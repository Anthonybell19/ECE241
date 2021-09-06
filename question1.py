class Hw1q1:
    def timeConvert(input_second : int):
        if (input_second//86400) > 1:
            days = (input_second//86400).__str__() + ' days,'
        elif (input_second//86400) == 1:
            days = (input_second // 86400).__str__() + ' day,'
        else:
            days = ''

        input_second = (input_second % 86400)

        if (input_second//3600) > 1:
            hours = (input_second//3600).__str__() + ' hours,'
        elif (input_second//3600) == 1:
            hours = (input_second//3600).__str__() + ' hours,'
        else:
            hours = ''

        input_second = (input_second % 3600)

        if (input_second//60) > 1:
            minutes = (input_second//60).__str__() + ' minutes,'
        elif (input_second//60) == 1:
            minutes = (input_second//60).__str__() + ' minute,'
        else:
            minutes = ''

        input_second = (input_second % 60)

        if input_second > 1:
            seconds = input_second.__str__() + ' seconds.'
        elif input_second == 1:
            seconds = input_second.__str__() + ' second.'
        else:
            seconds = ''

        return days + ' ' + hours + ' ' + minutes + ' ' + seconds


def main():
    print(Hw1q1.timeConvert(60))


# __name__
if __name__ == "__main__":
    main()
