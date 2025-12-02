import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(41)

# 定义文件夹路径
code_folder = os.path.dirname(os.path.abspath(__file__))
data_folder = os.path.join(code_folder, '..', 'data')

# 确保 data 文件夹存在
os.makedirs(data_folder, exist_ok=True)

# 定义生成数据的函数
def generate_data(filename, rows, cols, min_val, max_val, conditions=None):
    data = np.random.uniform(min_val, max_val, (rows, cols))

    if conditions:
        for condition in conditions:
            col, threshold, percentage = condition
            num_to_change = int(rows * percentage)
            indices_to_change = np.random.choice(rows, num_to_change, replace=False)
            data[indices_to_change, col] = np.random.uniform(threshold, max_val, num_to_change)

    # 保存数据到文件
    filepath = os.path.join(data_folder, filename)
    np.savetxt(filepath, data, fmt='%.9f', delimiter=',')
    print(f"Generated {filename} with {rows} rows and {cols} columns.")

def generate_student_abilities(num_students=200):
    students = pd.DataFrame(index=range(num_students))

    academic = np.clip(np.random.normal(0.45, 0.15, num_students), 0.10, 0.70)
    programming = np.clip(0.7*academic + 0.4*np.random.normal(0.40, 0.13, num_students), 0.10, 0.70)
    writing = np.clip(0.6*academic + 0.4*np.random.normal(0.42, 0.12, num_students), 0.10, 0.70)
    math = np.clip(0.82*academic + 0.18*np.random.normal(0.48, 0.10, num_students), 0.10, 0.70)
    english = np.clip(0.63*academic + 0.37*np.random.normal(0.42, 0.11, num_students), 0.10, 0.70)

    communication = np.random.beta(2.3, 2.7, num_students)
    cooperation = np.random.beta(2.3, 2.7, num_students)

    # leadership：确保 ≈80% ≥ 0.4
    leadership = np.random.beta(3.0, 2.0, num_students)
    threshold = np.quantile(leadership, 0.20)
    leadership = np.where(
        leadership < threshold,
        0.32 + np.random.uniform(0, 0.08, leadership.shape[0]),
        leadership
    )
    leadership = np.clip(leadership, 0.18, 0.80)

    confidence = np.clip(0.75*academic + 0.25*np.random.normal(0.42, 0.10, num_students), 0.10, 0.72)

    students["academic"] = academic
    students["programming"] = programming
    students["writing"] = writing
    students["math"] = math
    students["english"] = english
    students["communication"] = communication
    students["leadership"] = leadership
    students["cooperation"] = cooperation
    students["confidence"] = confidence

    return students


if __name__ == "__main__":

    students = generate_student_abilities(200)
    # 生成人格文件
    personality_conditions = [
        (2, 0.55, 0.8),  # 第3列，80%的人不低于0.55
        (3, 0.7, 0.75)    # 第4列，75%的人不低于0.7
    ]
    generate_data("personality.txt", 200, 5, 0, 1, conditions=personality_conditions)

    # 生成学习风格文件（4列，空格分隔）
    learning_style_data = np.random.uniform(0, 0.5, (200, 4))
    filepath = os.path.join(data_folder, "learning_style.txt")
    np.savetxt(filepath, learning_style_data, fmt='%.9f', delimiter=' ')
    print(f"Generated learning_style.txt with 200 rows and 4 columns (space-separated).")

    print("\n完成。")
