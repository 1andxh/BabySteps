import time

def glock(ammo):
    if ammo < 0:
        return
    time.sleep(0.3)
    print(f"piw piw!! \n bullets: {ammo}")
    return glock(ammo - 1)


glock(19)
print("RELOAD!")