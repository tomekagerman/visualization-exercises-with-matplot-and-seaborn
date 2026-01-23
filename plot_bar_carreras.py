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

# Plot
plt.figure(figsize=(8, 5))
colors = sns.color_palette('Set2', n_colors=len(df_carreras))
plt.bar(df_carreras['Carrera'], df_carreras['Estudiantes'], color=colors)
plt.xlabel('Major')
plt.ylabel('Number of students')
plt.title('Students per Major')
plt.grid(axis='y', alpha=0.3)
for i, v in enumerate(df_carreras['Estudiantes']):
    plt.text(i, v + 2, str(v), ha='center')
plt.tight_layout()
out_path = 'students_per_major.png'
plt.savefig(out_path)
print(f'Saved {out_path}')
