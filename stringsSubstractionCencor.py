# для цензуры
class Deleting_string:
    @staticmethod
    def delete(text: str, minus: str) -> str:
        new = []
        n = 0
        Flag = False

        for i in text:
            for x in minus[n]:
                if i != x:
                    new.append(i)
                    n -= 1
                    break
                elif i == x and minus in text:
                    break
                else:
                    new.append(i)
                    n -= 1
                    break
            if n < len(minus)-1:
                n += 1
            else:
                # Flag = True
                n = 0

        return (''.join(new))

    # # -------TESTs---------

    assert delete('spiderman', 'spi') == 'derman'
    assert delete('rafael raf', 'raf') == 'ael '
    assert delete('goverment', 'govno') == 'goverment'

    # # ------------------------