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

# Create pie chart
plt.figure(figsize=(8, 6))
colors = sns.color_palette('Set2', n_colors=len(df_carreras))
plt.pie(df_carreras['Estudiantes'], 
        labels=df_carreras['Carrera'], 
        autopct='%1.1f%%',
        colors=colors,
        startangle=90)
plt.title('Distribution of Students by Major')
plt.axis('equal')
plt.tight_layout()
out_path = 'students_distribution_pie.png'
plt.savefig(out_path)
print(f'Saved {out_path}')
print("Pie chart created successfully!")
