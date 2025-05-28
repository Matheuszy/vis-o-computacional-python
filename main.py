import cv2 as cv
import mediapipe as mp
import time
import pyautogui

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

from mediapipe.framework.formats import landmark_pb2

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

model_path = './modelo/hand_landmarker.task'

detection_result = None

def print_result(result: HandLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    global detection_result
    detection_result = result

# --- Inicialização do HandLandmarker ---
options = HandLandmarkerOptions(
    base_options = BaseOptions(model_asset_path=model_path),
    running_mode = VisionRunningMode.LIVE_STREAM,
    result_callback=print_result
)

landmarker = HandLandmarker.create_from_options(options)

# --- Inicialização da Câmera ---
capture = cv.VideoCapture(0)

if not capture.isOpened():
    print("Não foi possível abrir a câmera.")
    exit()

print("Câmera acessada com sucesso. Mostrando feed de vídeo. Pressione 'q' para sair na janela OpenCV.")

# --- Configurações do PyAutoGUI ---
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0

LARGURA_TELA_SISTEMA, ALTURA_TELA_SISTEMA = pyautogui.size()
print(f"Dimensões da tela do sistema: {LARGURA_TELA_SISTEMA}x{ALTURA_TELA_SISTEMA}")

# --- LOOP PRINCIPAL COM 'while True' ---
while True:
    ret, quadro = capture.read()

    if not ret:
        print("Não é possível fazer a captura do quadro. Fechando o programa.")
        break

    quadro = cv.flip(quadro, 1)

    rgb_frame = cv.cvtColor(quadro, cv.COLOR_BGR2RGB)

    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    frame_timestamp_ms = int(time.time() * 1000)

    landmarker.detect_async(mp_image, frame_timestamp_ms)

    if detection_result and detection_result.hand_landmarks:
        hand_landmarks_single_hand = detection_result.hand_landmarks[0] 

        landmarks_for_drawing = landmark_pb2.NormalizedLandmarkList()
        for landmark in hand_landmarks_single_hand:
            landmarks_for_drawing.landmark.add(x=landmark.x, y=landmark.y, z=landmark.z)

        mp_drawing.draw_landmarks(
            quadro,
            landmarks_for_drawing,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
            mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)
        )

        ponto_controle = hand_landmarks_single_hand[8] 
        
        coord_x_mouse = int((1 - ponto_controle.x) * LARGURA_TELA_SISTEMA)
        coord_y_mouse = int(ponto_controle.y * ALTURA_TELA_SISTEMA)

        pyautogui.moveTo(coord_x_mouse, coord_y_mouse)

    cv.imshow('Feed da Câmera com Detecção de Maos', quadro)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# --- Liberação de Recursos ---
capture.release()
landmarker.close()
cv.destroyAllWindows()
print("Processo finalizado.")