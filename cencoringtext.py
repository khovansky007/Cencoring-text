from stringsSubstractionCencor import Deleting_string as dt

class –°encorText:

    def __init__(self, UnCencoredText: str, curse: list[str]) -> None:
        self._text = UnCencoredText
        self.edittext = UnCencoredText
        self.curse = curse

        self.edit(self._text, self.deleteMats())

    def deleteMats(self) -> str:
        for curse in self.curse:
            while curse in self.edittext:
                self.edittext = dt.delete(self.edittext, curse)
                break
            continue
        if self.edittext == '':
            self.edittext = self.edittext  +  ' '

        return self.edittext
        


    def edit(self, UnCencoredText: str, EditText: str) -> None:
        new = []
        n = 0
        Flag = 0

        for i in UnCencoredText:
            for x in EditText[n]:
                
                if i != x:
                    new.append('*')
                    break
                else:
                    new.append(i)
                    if n > len(EditText) - 1:
                        new.append(i)
                    if n != len(EditText) - 1:
                        n += 1
                    break
                
            # if Flag == 1:
            #     break
            continue
        
        self.cencoredText = ''.join(new)
