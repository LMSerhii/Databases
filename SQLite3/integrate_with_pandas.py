import pandas as pd

from main import cursor

df_skill = pd.DataFrame(
    {
        'user_id': [1, 1, 2, 2, 3, 3, 3],
        'skill': ['Network Security', 'Algorithm Development', 'Network Security',
                  'Java', 'Python', 'Data Science', 'Machine Learning']
    }
)
# print(df_skill)

df_skill.to_sql('SKILL', cursor)

df = pd.read_sql("""
    SELECT s.user_id, u.name, u.age, s.skill
    FROM USER u LEFT JOIN SKILL s ON u.id = s.user_id
""", cursor)

print(df)
