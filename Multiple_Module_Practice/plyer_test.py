from plyer import notification
import time
import winsound


def notify_me(title, message):
    time.sleep(2)
    notification.notify(
        title=title,
        message=message,
        app_icon="./life_animal_squid_sea_octopus_icon_209493.ico",
        timeout=10)
    winsound.PlaySound("sound.wav", winsound.SND_ASYNC)




notify_me("TEST", "NOTIFICATION WORKED")


