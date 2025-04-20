import psycopg2
import csv
import os

# 连接 PostgreSQL 数据库
conn = psycopg2.connect(
    database="Phonebook",  # 数据库名称
    user="postgres",       # 用户名
    password="1234",       # 密码
    host="localhost",      # 主机地址
    port="5432"            # 端口号
)

cur = conn.cursor()

# 从 CSV 文件中导入数据
def insert_from_csv(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if not row or len(row) < 2:
                    continue  # 跳过空行或格式不完整的行
                name, phone = row[0], row[1]

                # 查重，避免重复插入
                cur.execute("SELECT 1 FROM contacts WHERE name = %s AND phone_number = %s", (name, phone))
                if cur.fetchone():
                    print(f"⚠️ 联系人已存在：{name}，跳过")
                    continue

                try:
                    cur.execute("INSERT INTO contacts (name, phone_number) VALUES (%s, %s)", (name, phone))
                    print(f"✅ 成功导入联系人：{name}")
                except Exception as e:
                    print(f"❌ 插入失败 {row}：{e}")
        conn.commit()
        print("📥 CSV 数据导入完成。")
    except Exception as e:
        print(f"❗ 读取 CSV 或导入数据出错：{e}")
        conn.rollback()

# 手动输入添加联系人
def insert_from_input():
    try:
        name = input("请输入联系人姓名：")
        phone = input("请输入联系人电话号码：")
        cur.execute("INSERT INTO contacts (name, phone_number) VALUES (%s, %s)", (name, phone))
        conn.commit()
        print("✅ 新联系人已添加。")
    except Exception as e:
        print(f"❌ 添加联系人失败：{e}")
        conn.rollback()

# 根据 ID 更新联系人
def update_contact():
    try:
        contact_id = input("请输入要更新的联系人 ID：")
        new_name = input("请输入新的姓名：")
        new_phone = input("请输入新的电话号码：")
        cur.execute("UPDATE contacts SET name = %s, phone_number = %s WHERE id = %s", (new_name, new_phone, contact_id))
        conn.commit()
        print("✅ 联系人信息已更新。")
    except Exception as e:
        print(f"❌ 更新失败：{e}")
        conn.rollback()

# 根据关键词查询联系人
def query_with_filter():
    try:
        keyword = input("请输入姓名或电话号码关键词：")
        cur.execute("SELECT * FROM contacts WHERE name ILIKE %s OR phone_number ILIKE %s", (f'%{keyword}%', f'%{keyword}%'))
        rows = cur.fetchall()
        if rows:
            print("🔎 查询结果：")
            for row in rows:
                print(row)
        else:
            cur.execute("SELECT * FROM search_contact(%s);", (keyword,))
    except Exception as e:
        print(f"❌ 查询失败：{e}")

def query_with_pagination():
    try:
        limit = int(input("Enter limit: "))
        offset = int(input("Enter offset: "))
        cur.execute("SELECT * FROM get_paginated_records2(%s, %s);", (limit, offset))
        for row in cur.fetchall():
            print(row)
        cur.close()
        conn.close()
    except Exception as e:
        print(f"❌ 查询失败：{e}")

        
# 根据 ID 删除联系人
def delete_contact():
    try:
        contact_id = input("请输入要删除的联系人 ID：")
        cur.execute("DELETE FROM contacts WHERE id = %s", (contact_id,))
        conn.commit()
        print("🗑️ 联系人已删除。")
    except Exception as e:
        print(f"❌ 删除失败：{e}")
        conn.rollback()

# 主菜单
def menu():
    run = True
    while run:
        print("\n📒 电话簿菜单：")
        print("1 - 从 CSV 文件导入联系人")
        print("2 - 手动输入添加联系人")
        print("3 - 更新联系人信息")
        print("4 - 查询联系人")
        print("5 - 删除联系人")
        print("6 - 退出程序")
        print('7 - pagination')

        choice = input("请选择操作（1-6）：")

        if choice == '1':
            insert_from_csv(r'C:\Users\Bakobe\OneDrive\Desktop\labaratory works\LAB11\newp.csv')  # CSV 文件路径
        elif choice == '2':
            insert_from_input()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            query_with_filter()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            run = False
            print("👋 程序已退出，再见！")
        elif choice == '7':
            query_with_pagination()
        else:
            print("⚠️ 无效选项，请输入 1 到 6。")
        

# 运行程序
menu()

# 关闭数据库连接
cur.close()
conn.close()
