num=10
match num:
    case 10:
        print("num is 10")
    case 20:
        print("num is 20")
    case others:  # this is default case
        print("num is other than 10 and 20")

color="yellow"
match color:
    case "Red"|"yellow":  #this is for multiple values
        print("color is either red or yellow")
    case "green":
        print("the color is green")
    case _:  #this is default case
        print("The color is blue")
        
