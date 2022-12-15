class Deleting_string:
    @staticmethod
    def delete(text: str, minus: str) -> str:
        
        n = 0

        startSpace = 0
        countSpace = text.count(' ')
        listWordsText = [] # [str]
        for d in range(1, countSpace + 1 + 1):
            Flag = True
            while Flag == True:
                word = []
                for i in text:

                    if i != ' ':
                        word.append(i)
                    else:
                        Flag = False
                        break
                if d == countSpace + 1:
                    Flag = False
                    break
                
            listWordsText.append(''.join(word))
            text = text[len(word):]  # - (' ' + word)
            try:
                if text[0] == ' ':
                    text = text[1:]
            except:
                ...

       
        n = 0
        cencuredPhrase = []
        for word in listWordsText:
            cencuredWord = []
            for i in word:
                for x in minus[n]:
                    if i != x:
                        cencuredWord.append(i)
                        n -= 1
                        break
                    elif i == x and minus in word:
                        break
                    else:
                        cencuredWord.append(i)
                        n -= 1
                        break
                if n < len(minus)-1:
                    n += 1
                else:
                    n = 0

            cencuredPhrase.append(''.join(cencuredWord))

        responce = ''
        for i in range(len(cencuredPhrase)):
            responce += cencuredPhrase[i] + ' '
        responce = responce[:-1]


        

        return responce
