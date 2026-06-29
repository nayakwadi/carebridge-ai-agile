-- CareBridge — Data tier seed (synthetic, de-identified demo data only).
-- Runs after init.sql on first postgres boot. Safe to re-run: guarded by NOT EXISTS.
-- The backend's idempotent seeder sees these rows and skips, so data is never doubled.

INSERT INTO care_team_members (full_name, role, email, specialty)
SELECT * FROM (VALUES
    ('Dr. Amara Okafor',   'Physician',         'a.okafor@carebridge.example',   'Internal Medicine'),
    ('Liam Chen',          'Nurse',             'l.chen@carebridge.example',     'Med-Surg'),
    ('Priya Nair',         'Care Coordinator',  'p.nair@carebridge.example',     'Transitions of Care'),
    ('Marcus Webb',        'Social Worker',     'm.webb@carebridge.example',     'Behavioral Health'),
    ('Dr. Sofia Rossi',    'Pharmacist',        's.rossi@carebridge.example',    'Medication Reconciliation')
) AS v(full_name, role, email, specialty)
WHERE NOT EXISTS (SELECT 1 FROM care_team_members);

INSERT INTO patients (mrn, full_name, date_of_birth, primary_condition, risk_level, status)
SELECT * FROM (VALUES
    ('MRN-100247', 'Eleanor Whitfield', DATE '1948-03-12', 'Congestive Heart Failure', 'high',   'active'),
    ('MRN-100311', 'Theodore Banks',    DATE '1955-09-30', 'Type 2 Diabetes',          'medium', 'active'),
    ('MRN-100422', 'Rosa Delgado',      DATE '1967-01-22', 'COPD',                     'high',   'active'),
    ('MRN-100538', 'Henry Osei',        DATE '1972-07-05', 'Post-Op Hip Replacement',  'medium', 'active'),
    ('MRN-100644', 'Grace Lindqvist',   DATE '1989-11-18', 'Hypertension',             'low',    'active')
) AS v(mrn, full_name, date_of_birth, primary_condition, risk_level, status)
WHERE NOT EXISTS (SELECT 1 FROM patients);

-- Care plans (one per high/medium patient to keep the board lively).
INSERT INTO care_plans (patient_id, title, goal, status, start_date, target_date)
SELECT p.id, v.title, v.goal, v.status, v.start_date, v.target_date
FROM (VALUES
    ('MRN-100247', '30-Day CHF Readmission Prevention', 'Keep patient stable at home; avoid readmission within 30 days of discharge.', 'active', DATE '2026-06-01', DATE '2026-07-01'),
    ('MRN-100311', 'Diabetes Self-Management Ramp-Up',  'Achieve HbA1c < 7.5 and confident self-administered insulin within 8 weeks.',  'active', DATE '2026-05-20', DATE '2026-07-15'),
    ('MRN-100422', 'COPD Exacerbation Recovery',        'Restore baseline oxygen saturation and complete pulmonary rehab referral.',     'active', DATE '2026-06-10', DATE '2026-07-22'),
    ('MRN-100538', 'Hip Replacement Rehab Pathway',     'Regain mobility milestones and transition off home physical therapy.',          'active', DATE '2026-06-15', DATE '2026-08-01')
) AS v(mrn, title, goal, status, start_date, target_date)
JOIN patients p ON p.mrn = v.mrn
WHERE NOT EXISTS (SELECT 1 FROM care_plans);

-- Tasks across the Kanban columns for the first two care plans.
INSERT INTO tasks (care_plan_id, title, description, status, priority, assignee_id, due_date)
SELECT cp.id, v.title, v.description, v.status, v.priority, ctm.id, v.due_date
FROM (VALUES
    ('30-Day CHF Readmission Prevention', 'Schedule 48-hour post-discharge follow-up call', 'Nurse to confirm weight, symptoms, and medication adherence.', 'done',        'high',   'Liam Chen',       DATE '2026-06-03'),
    ('30-Day CHF Readmission Prevention', 'Medication reconciliation',                      'Pharmacist to reconcile discharge meds against home list.',     'in_progress', 'urgent', 'Dr. Sofia Rossi', DATE '2026-06-05'),
    ('30-Day CHF Readmission Prevention', 'Arrange home scale + daily weight log',          'Coordinate DME delivery and patient education on daily weights.', 'todo',       'medium', 'Priya Nair',      DATE '2026-06-08'),
    ('30-Day CHF Readmission Prevention', 'Confirm cardiology appointment',                 'Specialist visit within 7 days; transport blocked pending insurance auth.', 'blocked', 'high', 'Priya Nair',  DATE '2026-06-09'),
    ('Diabetes Self-Management Ramp-Up',  'Insulin self-administration teach-back',         'Nurse-led session; document teach-back competency.',            'in_progress', 'high',   'Liam Chen',       DATE '2026-06-12'),
    ('Diabetes Self-Management Ramp-Up',  'Dietitian referral',                             'Refer for medical nutrition therapy.',                          'todo',        'medium', 'Marcus Webb',     DATE '2026-06-18'),
    ('Diabetes Self-Management Ramp-Up',  'Baseline HbA1c lab draw',                        'Order and collect baseline labs.',                              'done',        'medium', 'Dr. Amara Okafor',DATE '2026-05-22')
) AS v(plan_title, title, description, status, priority, assignee_name, due_date)
JOIN care_plans cp ON cp.title = v.plan_title
LEFT JOIN care_team_members ctm ON ctm.full_name = v.assignee_name
WHERE NOT EXISTS (SELECT 1 FROM tasks);
