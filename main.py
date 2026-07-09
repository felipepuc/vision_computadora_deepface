from deepface import DeepFace
import os

# Proyecto 2: Sistema de inicio de sesión seguro con verificación facial

IMAGEN_REGISTRADA = "rostros/usuario_registrado.jpg"
IMAGEN_LOGIN = "rostros/intento_login.jpg"


def verificar_login_facial():
    """
    Compara el rostro registrado con el rostro de intento de inicio de sesión.
    Si ambos rostros coinciden, se permite el acceso.
    """

    if not os.path.exists(IMAGEN_REGISTRADA):
        print("No se encontró la imagen del usuario registrado.")
        print("Coloca una imagen en: rostros/usuario_registrado.jpg")
        return

    if not os.path.exists(IMAGEN_LOGIN):
        print("No se encontró la imagen del intento de login.")
        print("Coloca una imagen en: rostros/intento_login.jpg")
        return

    resultado = DeepFace.verify(
        img1_path=IMAGEN_REGISTRADA,
        img2_path=IMAGEN_LOGIN,
        model_name="VGG-Face",
        enforce_detection=False
    )

    print("Resultado de la verificación facial:")
    print(resultado)

    if resultado["verified"]:
        print("ACCESO PERMITIDO: el rostro coincide con el usuario registrado.")
    else:
        print("ACCESO DENEGADO: el rostro no coincide con el usuario registrado.")


def analizar_emocion():
    """
    Analiza la emoción dominante del rostro usado para iniciar sesión.
    """

    if not os.path.exists(IMAGEN_LOGIN):
        print("No se encontró la imagen para analizar emociones.")
        return

    analisis = DeepFace.analyze(
        img_path=IMAGEN_LOGIN,
        actions=["emotion"],
        enforce_detection=False
    )

    if isinstance(analisis, list):
        analisis = analisis[0]

    print("Emoción dominante detectada:")
    print(analisis["dominant_emotion"])


if __name__ == "__main__":
    print("Sistema de inicio de sesión con verificación facial")
    print("-----------------------------------------------")

    verificar_login_facial()
    print()
    analizar_emocion()
