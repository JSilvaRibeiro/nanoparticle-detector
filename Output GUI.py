import tkinter as tk
from PIL import Image, ImageDraw, ImageFont
import cv2 , random , os
import matplotlib.pyplot as plt 
import numpy as np

def open_second_window():
  second_window = tk.Toplevel(root)
  second_window.title("Output")
  label = tk.Label(second_window, text= "Output Module")
  label.pack()
  # Add buttons to show black canvas and randomly plotted points
  """
  show_canvas = tk.Button(root, text="Show Canvas", command= get_img_dim)
  show_canvas.pack(pady=10)

  plot_particles_button = tk.Button(root, text ="Plot NanoParticles", command= plot_points)
  plot_particles_button.pack(pady=10)

  window_width = 400
  window_height = 250
  screen_width = second_window.winfo_screenwidth()
  screen_height = second_window.winfo_screenheight()
  x_coordinate = (screen_width/2) - (window_width/2)
  y_coordinate = (screen_height/2) - (window_height/2)
  root.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")
"""

def plot_points():
  canvas_size = 100
  canvas = [[0] * canvas_size for _ in range(canvas_size)]
  num_points = 50
  for _ in range(num_points):
    x = random.randint(0,canvas_size - 1)
    y = random.randint(0, canvas_size - 1)
    canvas[y][x] = 1
  
  plt.imshow(canvas, cmap= 'gray', origin ='lower')
  plt.title ('Random Points on Canvas')
  plt.show()

def plot_points_images():
  image = plt.imread('c:/Users/Dante/Pictures/Nanoparticle Test/test_img.jpeg')
  plt.imshow(image)
  plt.axis('off')
  num_points = 100
  max_x, max_y = image.shape[1], image.shape[0]
  random_x = np.random.randint(0 , max_x, size = num_points)
  random_y = np.random.randint(0 , max_y, size = num_points)

  plt.scatter(random_x, random_y, color ='red', s=10)

  plt.show()


def get_img_dim():
  image_path = 'c:/Users/Dante/Pictures/Nanoparticle Test/test_img.jpeg'
  image = Image.open(image_path)
  width, height = image.size
  print(f"Width : {width}, Height: {height}")
  black_image = Image.new("RGB", (width,height), "black")
  draw = ImageDraw.Draw(black_image)
  image.show()
  black_image.show()
  size = image.size
  return size


root = tk.Tk()
root.title("NanoLense")

title_label = tk.Label(root, text ="NanoLense", font=("Arial",16, "bold"))
title_label.pack(pady=10)

show_canvas = tk.Button(root, text="Show Canvas", command= get_img_dim)
show_canvas.pack(pady=10)

plot_particles_button = tk.Button(root, text ="Plot NanoParticles", command= plot_points)
plot_particles_button.pack(pady=10)

plot_points_on_images = tk.Button(root, text ="Plot Points on Image", command= plot_points_images)
plot_points_on_images.pack(pady=10)                     



window_width = 400
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width/2) - (window_width/2)
y_coordinate = (screen_height/2) - (window_height/2)
root.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

root.mainloop()


