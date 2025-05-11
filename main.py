from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

full_name = input("enter you full name: ")


image = Image.open("background.png")
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)

draw.text((350,100), "Corporation Of Nothing", font=font, fill="black")
draw.text((350,150), "Certificate of Absolute Shiet Programming SKills", font=font, fill="black")
draw.text((350,300), "This is to certify that", font=font, fill="black")
draw.text((350,300), full_name, font=font, fill="black")
draw.text((350,300), "For demonstrating an exceptional ability to: Write code that runs nowhere, Debug problems that don’t exist (and miss the ones that do), Master the ancient art of Googling Stack Overflow for the wrong error, And commit code so meaningless, Git itself questioned its purpose.", font=font, fill="black")
draw.text((350,500), f'Issued on {datetime.now().strftime("%B %d, %Y")}', font=font, fill="black")
draw.text((350,300), "Ms Defjoy", font=font, fill="black")
draw.text((350,300), "CEO OF THE WORST PROGRAMMING SKILLS", font=font, fill="black")


image.save("certificate.png")