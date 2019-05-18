def cetakGambar(banyakGambar):
    result=""

    for baris in range(banyakGambar):
        for kolom in range(banyakGambar):
            if (baris==kolom or kolom == banyakGambar - baris - 1):
                result+="X"
            else:
                result+="="
        result+="\n"

    return result

print(cetakGambar(7))
