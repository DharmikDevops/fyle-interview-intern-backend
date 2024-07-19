-- Write query to get number of graded assignments for each student:

-- number_of_graded_assignments_for_each_student.sql

SELECT
    student_id,
    COUNT(*) AS graded_assignments_count
FROM
    assignments
WHERE
    state = 'GRADED'
GROUP BY
    student_id;
