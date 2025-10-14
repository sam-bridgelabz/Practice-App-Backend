-- programme
INSERT INTO programme (id, name, created_at)
VALUES
('11111111-1111-1111-1111-111111111111', 'Java Mastery Programme', NOW(3));

-- module
INSERT INTO module (id, programme_id, name, created_at)
VALUES
('22222222-2222-2222-2222-222222222222', '11111111-1111-1111-1111-111111111111', 'Core Java', NOW(3)),
('33333333-3333-3333-3333-333333333333', '11111111-1111-1111-1111-111111111111', 'Advanced Java', NOW(3)),
('44444444-4444-4444-4444-444444444444', '11111111-1111-1111-1111-111111111111', 'Java Frameworks', NOW(3)),
('55555555-5555-5555-5555-555555555555', '11111111-1111-1111-1111-111111111111', 'Java Interview Prep', NOW(3));


-- topic
INSERT INTO topic (id, module_id, name, created_at)
VALUES
('66666666-6666-6666-6666-666666666666', '22222222-2222-2222-2222-222222222222', 'OOP Concepts', NOW(3)),
('77777777-7777-7777-7777-777777777777', '22222222-2222-2222-2222-222222222222', 'Exception Handling', NOW(3)),
('88888888-8888-8888-8888-888888888888', '33333333-3333-3333-3333-333333333333', 'Collections Framework', NOW(3)),
('99999999-9999-9999-9999-999999999999', '33333333-3333-3333-3333-333333333333', 'Multithreading', NOW(3)),
('aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa', '44444444-4444-4444-4444-444444444444', 'Streams and Lambdas', NOW(3)),
('bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb', '33333333-3333-3333-3333-333333333333', 'Memory Management', NOW(3)),
('cccccccc-cccc-cccc-cccc-cccccccccccc', '44444444-4444-4444-4444-444444444444', 'Design Patterns', NOW(3)),
('dddddddd-dddd-dddd-dddd-dddddddddddd', '33333333-3333-3333-3333-333333333333', 'File Handling', NOW(3)),
('eeeeeeee-eeee-eeee-eeee-eeeeeeeeeeee', '44444444-4444-4444-4444-444444444444', 'Functional Programming', NOW(3)),
('ffffffff-ffff-ffff-ffff-ffffffffffff', '55555555-5555-5555-5555-555555555555', 'Concurrency & Threads', NOW(3));


-- subtopic
INSERT INTO subtopic (id, topic_id, name, created_at)
VALUES
('s1a11111-aaaa-aaaa-aaaa-aaaaaaaaaaaa', '66666666-6666-6666-6666-666666666666', 'Inheritance and Polymorphism', NOW(3)),
('s2b22222-bbbb-bbbb-bbbb-bbbbbbbbbbbb', '77777777-7777-7777-7777-777777777777', 'Try-Catch-Finally Blocks', NOW(3)),
('s3c33333-cccc-cccc-cccc-cccccccccccc', '88888888-8888-8888-8888-888888888888', 'ArrayList and LinkedList', NOW(3)),
('s4d44444-dddd-dddd-dddd-dddddddddddd', '99999999-9999-9999-9999-999999999999', 'Thread Lifecycle and Synchronization', NOW(3)),
('s5e55555-eeee-eeee-eeee-eeeeeeeeeeee', 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa', 'Lambda Expressions Basics', NOW(3)),
('s6f66666-ffff-ffff-ffff-ffffffffffff', 'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb', 'Garbage Collection Types', NOW(3)),
('s7g77777-gggg-gggg-gggg-gggggggggggg', 'cccccccc-cccc-cccc-cccc-cccccccccccc', 'Singleton and Factory Patterns', NOW(3)),
('s8h88888-hhhh-hhhh-hhhh-hhhhhhhhhhhh', 'dddddddd-dddd-dddd-dddd-dddddddddddd', 'FileReader and BufferedReader', NOW(3)),
('s9i99999-iiii-iiii-iiii-iiiiiiiiiiii', 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeeee', 'Streams API Operations', NOW(3)),
('s0j00000-jjjj-jjjj-jjjj-jjjjjjjjjjjj', 'ffffffff-ffff-ffff-ffff-ffffffffffff', 'Thread Communication & Executors', NOW(3));

-- questions
INSERT INTO questions (
    id, programme_id, module_id, topic_id, subtopic_id,
    question_type, answer_type, difficulty,
    stem_md, solution_md, score_weight,
    metadata_json, version, is_current, created_at, updated_at
)
VALUES
-- 1
(UUID(), '11111111-1111-1111-1111-111111111111', '22222222-2222-2222-2222-222222222222',
 '66666666-6666-6666-6666-666666666666', 's1a11111-aaaa-aaaa-aaaa-aaaaaaaaaaaa',
 'ASSIGNMENT', 'CODE', 'MEDIUM',
 'Write a Java program demonstrating runtime polymorphism using method overriding.',
 'Use a parent class Shape and subclasses Circle and Square overriding area().',
 5.00, JSON_OBJECT("tags", "java, oops, polymorphism"), 1, TRUE, NOW(3), NOW(3)),

-- 2
(UUID(), '11111111-1111-1111-1111-111111111111', '22222222-2222-2222-2222-222222222222',
 '77777777-7777-7777-7777-777777777777', 's2b22222-bbbb-bbbb-bbbb-bbbbbbbbbbbb',
 'ASSISTED', 'TEXT', 'EASY',
 'Explain the purpose of finally block in Java exception handling.',
 'It executes whether an exception occurs or not, mainly for resource cleanup.',
 3.00, JSON_OBJECT("tags", "java, exception-handling"), 1, TRUE, NOW(3), NOW(3)),

-- 3
(UUID(), '11111111-1111-1111-1111-111111111111', '33333333-3333-3333-3333-333333333333',
 '88888888-8888-8888-8888-888888888888', 's3c33333-cccc-cccc-cccc-cccccccccccc',
 'SELF', 'CODE', 'HARD',
 'Implement a Java class that mimics ArrayList functionality (add, get, remove).',
 'Use Object[] as base storage and dynamically resize when capacity is reached.',
 8.00, JSON_OBJECT("tags", "java, collections, arraylist"), 1, TRUE, NOW(3), NOW(3)),

-- 4
(UUID(), '11111111-1111-1111-1111-111111111111', '33333333-3333-3333-3333-333333333333',
 '99999999-9999-9999-9999-999999999999', 's4d44444-dddd-dddd-dddd-dddddddddddd',
 'TEST', 'TEXT', 'MEDIUM',
 'Differentiate between sleep() and wait() methods in Java threads.',
 'sleep() is static and doesn’t release lock; wait() releases lock and must be in synchronized block.',
 4.00, JSON_OBJECT("tags", "java, threads"), 1, TRUE, NOW(3), NOW(3)),

-- 5
(UUID(), '11111111-1111-1111-1111-111111111111', '44444444-4444-4444-4444-444444444444',
 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa', 's5e55555-eeee-eeee-eeee-eeeeeeeeeeee',
 'ASSIGNMENT', 'CODE', 'HARD',
 'Write a Java program using lambda expressions to filter even numbers from a list.',
 'Use List<Integer> and Stream.filter() to return only even numbers.',
 6.00, JSON_OBJECT("tags", "java, lambda, stream"), 1, TRUE, NOW(3), NOW(3)),

-- 6
(UUID(), '11111111-1111-1111-1111-111111111111', '33333333-3333-3333-3333-333333333333',
 'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb', 's6f66666-ffff-ffff-ffff-ffffffffffff',
 'ASSISTED', 'TEXT', 'EASY',
 'Explain how the garbage collector reclaims memory in Java.',
 'It removes unreferenced objects automatically to free heap space.',
 3.00, JSON_OBJECT("tags", "java, memory, gc"), 1, TRUE, NOW(3), NOW(3)),

-- 7
(UUID(), '11111111-1111-1111-1111-111111111111', '44444444-4444-4444-4444-444444444444',
 'cccccccc-cccc-cccc-cccc-cccccccccccc', 's7g77777-gggg-gggg-gggg-gggggggggggg',
 'SELF', 'CODE', 'MEDIUM',
 'Write Java code implementing the Singleton pattern with thread safety.',
 'Use double-checked locking with volatile instance and synchronized block.',
 5.00, JSON_OBJECT("tags", "java, design-patterns"), 1, TRUE, NOW(3), NOW(3)),

-- 8
(UUID(), '11111111-1111-1111-1111-111111111111', '33333333-3333-3333-3333-333333333333',
 'dddddddd-dddd-dddd-dddd-dddddddddddd', 's8h88888-hhhh-hhhh-hhhh-hhhhhhhhhhhh',
 'TEST', 'TEXT', 'HARD',
 'Describe how to handle file reading and writing efficiently in Java.',
 'Use try-with-resources and BufferedReader/BufferedWriter for efficient I/O.',
 7.00, JSON_OBJECT("tags", "java, io, file-handling"), 1, TRUE, NOW(3), NOW(3)),

-- 9
(UUID(), '11111111-1111-1111-1111-111111111111', '44444444-4444-4444-4444-444444444444',
 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeeee', 's9i99999-iiii-iiii-iiii-iiiiiiiiiiii',
 'ASSIGNMENT', 'CODE', 'MEDIUM',
 'Write a Java program demonstrating use of Stream.map() and collect().',
 'Use a list of strings and convert them to uppercase using Stream API.',
 5.00, JSON_OBJECT("tags", "java, streams"), 1, TRUE, NOW(3), NOW(3)),

-- 10
(UUID(), '11111111-1111-1111-1111-111111111111', '55555555-5555-5555-5555-555555555555',
 'ffffffff-ffff-ffff-ffff-ffffffffffff', 's0j00000-jjjj-jjjj-jjjj-jjjjjjjjjjjj',
 'SELF', 'TEXT', 'MEDIUM',
 'Explain the purpose of the Executor framework in Java concurrency.',
 'It provides a higher-level replacement for manually managing threads.',
 4.00, JSON_OBJECT("tags", "java, concurrency, executors"), 1, TRUE, NOW(3), NOW(3));
