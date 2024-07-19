-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
-- count_grade_A_assignments_by_teacher_with_max_grading.sql

WITH TeacherGradingCount AS (
    SELECT
        teacher_id,
        COUNT(*) AS graded_count
    FROM
        assignments
    WHERE
        state = 'GRADED'
    GROUP BY
        teacher_id
)
SELECT
    COUNT(*) AS count_grade_A_assignments
FROM
    assignments
WHERE
    teacher_id = (SELECT teacher_id FROM TeacherGradingCount ORDER BY graded_count DESC LIMIT 1)
    AND grade = 'A';
