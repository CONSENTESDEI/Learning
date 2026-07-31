"""
管理员教务系统开发：
    1. 添加写生成绩：输入姓名、语、数、英
    2. 修改学生成绩：输入姓名，修改成绩
    3. 删除学生成绩：输入姓名，删除成绩
    4. 查询指定学生成绩：输入姓名，查成绩
    5. 展示全部学生成绩：展示所有成绩
"""

# 学生类

class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return (f"姓名：{self.name} | "
                f"语文：{self.chinese} | "
                f"数学：{self.math} | "
                f"英语：{self.english} | "
                f"总分：{self.chinese + self.math + self.english}")

    def update_score(self, chinese = None, math = None, english = None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

# 教务系统类
class EduMangement:
    sys_ver = "1.0"
    sys_name = "教务管理系统"

    def __init__(self):
        self.student_list = []

    # 添加学生成绩
    def add_student(self, student):
        name = input("请输入学生姓名")

        # 判断学生是否存在
        for s in self.student_list:
            if s.name == name:
                print(f"学生存在，添加失败")
                return

        chinese = int(input("请输入语文成绩"))
        math = int(input("请输入数学成绩"))
        english = int(input("请输入英语成绩"))

        # 添加成绩
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name, chinese, math, english)
            self.student_list.append(stu)
            print(f"学生信息添加成功")
        else:
            print(f"成绩区间为1-100，添加失败")

    # 修改学生成绩
    def update_student(self):
        name = input("请输入要修改成绩的学生姓名")
        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩为：{s}")

                chinese = int(input("请输入语文成绩"))
                math = int(input("请输入数学成绩"))
                english = int(input("请输入英语成绩"))

                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese, math, english)
                    print(f"学生成绩修改成功")
                    print(f"修改后成绩为：{s}")
                    return
                else:
                    print(f"成绩区间为1-100，修改失败")
                    return
        print(f"未找到该学生！修改失败")

    # 删除学生成绩
    def del_student(self):
        name = input("请输入要删除的学生姓名")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print(f"学生信息删除成功。")
                return
        print(f"未找到该学生，删除失败。")

    # 查询指定学生成绩
    def query_student(self):
        name = input("请输入要查询的学生姓名")
        for s in self.student_list:
            if s.name == name:
                print(f"学生信息：{s}")
                return
        print(f"未找到该学生。")

    # 展示全部学生成绩
    def list_print(self):
        for s in self.student_list:
            print(f"{s}")

    # 系统运行
    def run_sys(self):
        print(f"欢迎使用教务管理系统 V{EduMangement.sys_ver}")

        while True:
            print()
            print(f"--------------------------------------")
            print(f"#               1.添加学生            #\n"
                  f"#               2.修改学生            #\n"
                  f"#               3.删除学生            #\n"
                  f"#               4.查询指定学生         #\n"
                  f"#               5.查询所有学生         #\n"
                  f"#               6.推出系统            #")
            print(f"--------------------------------------")

            choice = int(input("请输入1-6"))

            match choice:
                case 1:
                    self.add_student()
                case 2:
                    self.update_student()
                case 3:
                    self.del_student()
                case 4:
                    self.query_student()
                case 5:
                    self.list_print()
                case 6:
                    break
                case _:
                    print(f"输入错误")
                    continue

# 测试
if __name__ == '__main__':
    edu_mangement = EduMangement()
    edu_mangement.run_sys()



















