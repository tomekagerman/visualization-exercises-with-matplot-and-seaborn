import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Dataset
df_carreras = pd.DataFrame({
    'Carrera': ['Ingeniería', 'Medicina', 'Derecho', 'Psicología'],
    'Estudiantes': [120, 80, 60, 100]
})

# Create horizontal bar chart
plt.figure(figsize=(8, 5))
colors = sns.color_palette('Set2', n_colors=len(df_carreras))
plt.barh(df_carreras['Carrera'], df_carreras['Estudiantes'], color=colors)
plt.xlabel('Number of students')
plt.ylabel('Major')
plt.title('Students per Major (Horizontal)')
plt.grid(axis='x', alpha=0.3)
for i, v in enumerate(df_carreras['Estudiantes']):
    plt.text(v + 2, i, str(v), va='center')
plt.tight_layout()
out_path = 'students_per_major_horizontal.png'
plt.savefig(out_path)
print(f'Saved {out_path}')
print("Horizontal bar chart created successfully!")
