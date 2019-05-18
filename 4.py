def cetakGambar(banyakGambar):
    result=""

    for baris in range(banyakGambar):
        for kolom in range(banyakGambar):
            if (baris==kolom or kolom == banyakGambar - baris - 1):
<<<<<<< HEAD
<<<<<<< HEAD
                result+="X "
            else:
                result+="= "
=======
                result+="X"
            else:
                result+="="
>>>>>>> f68572953e4e6e50a706ccc42f5d81dcfa5da71e
=======
                result+="X"
            else:
                result+="="
>>>>>>> f68572953e4e6e50a706ccc42f5d81dcfa5da71e
        result+="\n"

    return result

print(cetakGambar(7))
