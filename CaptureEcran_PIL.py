import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
import imutils
import mss
import win32gui,  win32ui,  win32con, win32api



def capture_ecran_PIL(): 
    dernier_temps = time.time()
    while(True):
        # 1280*720 mode
        screenshot =  np.array(ImageGrab.grab(bbox=(0,40,1280,760)))
        new_screen = process_img(screenshot)
        print(f'{time.time()-dernier_temps} seconds - FPS = {1/(time.time()-dernier_temps)}')
        dernier_temps = time.time()

        cv2.imshow('window2',new_screen)

        """cv2.imshow('window',cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB))"""

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


def capture_ecran_AutoGUI():
    dernier_temps = time.time()
    while(True):
        im = np.array(pyautogui.screenshot(region=(0,40, 1280, 720)))
        print(f'{time.time()-dernier_temps} seconds - FPS = {1/(time.time()-dernier_temps)}')
        dernier_temps = time.time()
        cv2.imshow('window',cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


def capture_ecran_MSS_V1():
    dernier_temps = time.time()
    while (True):
        monitor = {'top': 40, 'left': 0, 'width': 1280, 'height': 710}
        sct = mss.mss()
        img = np.asarray(sct.grab(monitor))
        print(f'{time.time()-dernier_temps} seconds - FPS = {1/(time.time()-dernier_temps)}')
        dernier_temps = time.time()
        cv2.imshow('window',cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

def capture_ecran_MSS_V2():
    dernier_temps = time.time()
    while (True):
        monitor = {'top': 40, 'left': 0, 'width': 1280, 'height': 710}
        sct = mss.mss()
        img = np.asarray(sct.grab(monitor))
        print(f'{time.time()-dernier_temps} seconds - FPS = {1/(time.time()-dernier_temps)}')
        dernier_temps = time.time()
        cv2.imshow('window',cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

def capture_ecran_Win32_V1():
    dernier_temps = time.time()
    while (True):
        hwnd = win32gui.GetDesktopWindow()
        l, t, r, b = win32gui.GetWindowRect(hwnd)
        w = 1280
        h = 720

        hwindc = win32gui.GetWindowDC(hwnd)
        srcdc = win32ui.CreateDCFromHandle(hwindc)
        memdc = srcdc.CreateCompatibleDC()
        bmp = win32ui.CreateBitmap()
        bmp.CreateCompatibleBitmap(srcdc, w, h)
        memdc.SelectObject(bmp)
        memdc.BitBlt((0, 0), (w, h), srcdc, (l, 30), win32con.SRCCOPY)

        signedIntsArray = bmp.GetBitmapBits(False)
        img = np.array(signedIntsArray).astype(dtype="uint8")
        img.shape = (h,w,4)

        srcdc.DeleteDC()
        memdc.DeleteDC()
        win32gui.ReleaseDC(hwnd, hwindc)
        win32gui.DeleteObject(bmp.GetHandle())

        print(f'{time.time()-dernier_temps} seconds - FPS = {1/(time.time()-dernier_temps)}')
        dernier_temps = time.time()
        cv2.imshow('window',cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

def capture_ecran_Win32_V2():
    dernier_temps = time.time()
    while (True):
        hwnd = win32gui.GetDesktopWindow()
        l, t, r, b = win32gui.GetWindowRect(hwnd)
        w = 1280
        h = 720

        hwindc = win32gui.GetWindowDC(hwnd)
        srcdc = win32ui.CreateDCFromHandle(hwindc)
        memdc = srcdc.CreateCompatibleDC()
        bmp = win32ui.CreateBitmap()
        bmp.CreateCompatibleBitmap(srcdc, w, h)
        memdc.SelectObject(bmp)
        memdc.BitBlt((0, 0), (w, h), srcdc, (l, 30), win32con.SRCCOPY)

        signedIntsArray = bmp.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (h,w,4)

        srcdc.DeleteDC()
        memdc.DeleteDC()
        win32gui.ReleaseDC(hwnd, hwindc)
        win32gui.DeleteObject(bmp.GetHandle())

        print(f'{time.time()-dernier_temps} seconds - FPS = {1/(time.time()-dernier_temps)}')
        dernier_temps = time.time()
        cv2.imshow('window',cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break        


def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    return processed_img