import win32gui
import win32ui
import win32con
import win32api
#First we acquire a handle to the entire desktop which include the entire viewable area across multiple monitors
#grab handle to the main desktop window
hdesktop   = win32gui.GetDesktopWindow()
#we then determine the size of the size of the screen so that we know the dimensions required for the screenshots
#determine the size of all monitors in pixels
width      = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
height     = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
left       = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
right      = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
#create a device context
#we create a device context using GetWindowDC function call and pass in handle to our dsktop
desktop_dc = win32gui.GetWindowDC(hdesktop)
img_dc     = win32ui.CreateDCFromHandle(desktop_dc)
#create a memory based device context
#now we create a memory-based device context where we will store our image capture until we store the bbitmap bytes to a file.
mem_dc     = img_dc.CreateCompatibleDC()
#create a bitmap object
#we then create bitmap object that is set to the device context of our desktop
#The select object call then sets the memory-based device context to point at the bitmap thet we're capturing
screenshot = win32ui.CreateBitmap()
screenshot.CreateCompatibleBitmap(img_dc ,width ,height)
mem_dc.SelectObject(screenshot)
#copy the screen into our memory device context
#we use BitBlt function to take a bit-for-bit copy of the dekstop image and store it in the memory based contest.
mem_dc.BitBlt((0 ,0) ,(width ,height) ,img_dc ,(left ,right) ,win32con.SRCCOPY)
#Save the bitmap to a file
#the final step is to dump the shot
screenshot.SaveBitmapFile(mem_dc ,'C:\\WINDOWS\\TEMP\\screenshot.bmp')
#free our objects
mem_dc.DeleteDC()
win32gui.DeleteObject(screenshot.GetHandle())


 