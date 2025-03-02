with open("example.txt", "r") as src, open("baga.txt", "w") as dst: 
    dst.write(src.read())