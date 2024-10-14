def caeser_cipher(command, msg, shift):

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    final_text = ""

    if command == "decode":
        shift *= -1

    for letter in msg:
        position = alphabet.index(letter)
        new_position = position + shift
        final_text += alphabet[new_position]

    print(f'Resultado: {final_text}')

continuar = True

while continuar:
    fst_command = str(input("\"Encode\" or \"decode\": ")).lower()

    if fst_command != "encode" and fst_command != "decode":
        print("Essa opção não existe.")
    else:
        snd_command = str(input("Msg: ")).lower()
        thd_command = int(input("Shift: "))
        thd_command = thd_command % 26
        caeser_cipher(fst_command, snd_command, thd_command)
    loop = input("Continue the cipher? \"y\"|\"n\": ").lower()

    if loop == 'n':
        continuar = False