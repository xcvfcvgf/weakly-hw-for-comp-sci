menuChoice = input("Are you ready for magic? Please answer YES or NO")
        if menuChoice.lower() == ("yes"):
                menuChoice = input("Do you want the rubics cube turn clockwise or anticlockwise. Please enter TRUE for clockwise and NO for anti-clockwise")
                clockwise = menuChoice 
                
                r = ("red")
                w = ("white")
                y = ("yellow")
                o = ("orange")
                g = ("green")
                b = ("blue")
                
                face = [[r, w, r],
                        [g, o, y],
                        [w, r, b]]
                
                n = len(face)
                
                newFace = [[0] * n for k in range(n)]
                
                
                for i in range(0,n):
                    for j in range(0,n):
                            if clockwise.lower() == ("true"):
                                newFace[i][j] = face[n-1-j][i]
                            else:
                                newFace[i][j] = face[n-1-i][j]
                
                print(str(newFace))
        else:
                print("ok, bye")
