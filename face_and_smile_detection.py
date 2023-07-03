import cv2

# Carregar o classificador pré-treinado para detecção de rosto e sorriso
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

# Inicializar a captura de vídeo da câmera IP
ip = "https://192.168.0.2:8080/video"
video = cv2.VideoCapture(ip)

while True:
    # Ler o frame da captura de vídeo
    ret, frame = video.read()
    
    # Converter o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detectar rostos no frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        # Desenhar um retângulo ao redor do rosto detectado
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Recortar a região do rosto para detecção de sorriso
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
    # Detectar sorrisos na região do rosto
    smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.9, minNeighbors=40)
    
    # Se um sorriso for detectado, exibir a palavra "Feliz"
    for (x, y, w, h) in smiles:
        cv2.rectangle(roi_color, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(roi_color, 'Feliz', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    
    # Exibir o frame resultante
    cv2.imshow('Sorriso Detector', frame)
    
    # Verificar se a tecla 'q' foi pressionada para encerrar o programa
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar os recursos
video.release()
cv2.destroyAllWindows()