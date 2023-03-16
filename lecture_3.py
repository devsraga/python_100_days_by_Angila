print("Welcome to Roller Costar Ride")
name = input("Enter your name: ")
weight = float(input("Enter the total weight of your body in kilograms: "))
height = float(input("Enter your height in meters: "))
age = float(input("Enter your age in years: "))
print("Thank you " + name)
BMI = round(weight/height**2)
print(f"Aapka body mas indx BMI {BMI} hai")
if BMI < 18.5:
    print("You are under weight")
elif 18.5 <= BMI < 25:
    print("Your are fit")
    print('''
           /'
                           /
                          /
                          |_.._     _.-.
                          | -o-`   /-o-   \
                          |    '|         |
                          |               |
                          \      _        |
                           \   -'_`-      |
                            \         _.-' \
                             `--....-'      \
                               \             `\._
                               |\       /      .#`------.
                               ||    _ | -'   .#'        `\
                             _/.'  '        .#'            \
                        __..'              .#'              \
                     _.#                  .#'
                    /.#'              .#####
                   /.#'            .###'.#'#.
                   |#.          .##''  #' .###.    \
                  .#`###.     ,##'   `###.#' `#     \
                 .#'   `##.  ,#'   .##' `###.#'#     \
                #'       `#. #'..##''      `#'###     \
               ##.    ..#######''           .##'`#    /\
               # `######''.# #.           .##'   `###/  \
               `#        .#' `##,      ..##'##.     #
                `##.   ..#'    `##.  ..#'#####:F_P:#'
                  `#####''       `####'       ```###
                    `\`                            /
                      \                           /
''')
elif 25 >= BMI < 30:
    print("App over weight hain")
elif 30 >= BMI <= 35:
    print("Aap mote hain")
    print('''
               _.--._      
        ,'        `.   
       /   __) __`  \ 
      (   (`-`(-')   )
      /)  \   _  /  (
     /'    )-._.' .  \ ___
    (  ,--.,    `.)___(___)
     )(   /-.,--'\   _ \X/`
    '/ .'/        \ (  Uu")\
      / /          \ `/,-'  )
     ( ^      ,    ,^ )`._.'
      ( `.   Y   .'  )
       \  `. )\.'   / )
       )`._.'=='._.' (
      /               )   Ojo/VK/FS/ejm
     (                ."-.
    /(`    -)        /    \
   (  \`-.__    -'_."      `
   |  \`-.__.--"v"          |
   `.'      \   |,          ,
    /        `._/           :
   /           |           '
  /           /|          /
             / |         /
''')
else:
    print("Aap bahut jyada mote hain appko doctor ko dikhan ki jaroorat hai")
    print('''
               _.--._      
        ,'        `.   
       /   __) __`  \ 
      (   (`-`(-')   )
      /)  \   _  /  (
     /'    )-._.' .  \ ___
    (  ,--.,    `.)___(___)
     )(   /-.,--'\   _ \X/`
    '/ .'/        \ (  Uu")\
      / /          \ `/,-'  )
     ( ^      ,    ,^ )`._.'
      ( `.   Y   .'  )
       \  `. )\.'   / )
       )`._.'=='._.' (
      /               )   Ojo/VK/FS/ejm
     (                ."-.
    /(`    -)        /    \
   (  \`-.__    -'_."      `
   |  \`-.__.--"v"          |
   `.'      \   |,          ,
    /        `._/           :
   /           |           '
  /           /|          /
             / |         /
''')
