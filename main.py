import warnings
import universal
import db

warnings.filterwarnings("ignore")

stud = int(input("Введите кол-во студентов: "))
def students():
    i = 1
    while i < stud:
        study_direction = str(input("Введите направление подготовки студента: "))
        full_name = str(input("Введите ФИО: "))
        stu_numb = int(input("Введите номер студенческого билета: "))
        group_name = str(input("Введите группу: "))
        print("%2s %3s %4d %5s" % (study_direction, full_name, stu_numb, group_name))
        db.save_result(study_direction, full_name, stu_numb, group_name)
        i += 1
    return

def main():
    run = True
    commands = """==========================================================================
1. Создать таблицу и БД, результат сохранить в MySQL.
2. Ввести данные об учащемся, результат сохранить в MySQL.
3. Сохранить все данные из MySQL в Excel.
4. Завершить"""
    while run:
        run = universal.uni(commands,
                            db.check_db, students,
                            db.save_db_to_xlsx)
    return


if __name__ == '__main__':
    main()
