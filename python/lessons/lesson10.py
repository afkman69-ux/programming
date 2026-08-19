while True:

    number_of_student = int(input("number_of_student:  "))

    passed = 0
    failed = 0 
    total_score = 0

    for i in range(1, number_of_student + 1):

        print(f"student : {i}")

        name = input("name:  ")
        age = int(input("age:  "))
        score = float(input("score:  "))


        total_score += score

        if age < 18:
            print("too young")
        elif score >= 10:
            print("passed")
            passed += 1
        else:
            print("failed")
            failed += 1
        if score == 20:
            print("excellent!")
        elif score == 0:
            print("very bad!")


    avrage = total_score / number_of_student


    print("----- report -----")
    print(f"passed students: {passed}")
    print(f"failed students: {failed}")
    print(f"avrage: {avrage}")

    again = input("do you wana run the program again? yes/no  \n")

    if again == "yes":
        print("ok")
    elif again == "no":
        break