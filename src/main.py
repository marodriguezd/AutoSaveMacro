import pyautogui
import time

INTERVALO = 60 * 3


def save_automatically(interval=INTERVALO):
    """
    Simula la pulsación de CTRL-S cada ciertos segundos definidos por el intervalo.

    Args:
    interval (int): Número de segundos entre cada simulación de guardado.
    """
    while True:
        pyautogui.hotkey('ctrl', 's')  # Simula la pulsación de CTRL + S
        print("Guardado automático ejecutado.")
        print(f"Próximo guardado en {INTERVALO // 60} minutos.")
        time.sleep(interval)  # Espera el tiempo definido en el intervalo antes de repetir


if __name__ == "__main__":
    save_automatically(interval=INTERVALO)  # Configura el script para ejecutar el guardado cada 5 segundos
