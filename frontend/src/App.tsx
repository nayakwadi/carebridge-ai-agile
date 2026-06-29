import { useEffect, useState } from 'react'
import { api, type CarePlan, type Patient, type Stats, type Task, type TaskStatus } from './api/client'
import { CarePlanBoard } from './components/CarePlanBoard'
import { PatientList } from './components/PatientList'

const NEXT_STATUS: Record<TaskStatus, TaskStatus> = {
  todo: 'in_progress',
  in_progress: 'done',
  blocked: 'in_progress',
  done: 'todo',
}

export default function App() {
  const [patients, setPatients] = useState<Patient[]>([])
  const [stats, setStats] = useState<Stats | null>(null)
  const [selectedPatient, setSelectedPatient] = useState<Patient | null>(null)
  const [carePlans, setCarePlans] = useState<CarePlan[]>([])
  const [selectedPlan, setSelectedPlan] = useState<CarePlan | null>(null)
  const [tasks, setTasks] = useState<Task[]>([])
  const [error, setError] = useState<string | null>(null)

  // Initial load: patients + stats.
  useEffect(() => {
    api
      .patients()
      .then((p) => {
        setPatients(p)
        setSelectedPatient(p[0] ?? null)
      })
      .catch((e) => setError(String(e)))
    refreshStats()
  }, [])

  // When a patient is selected, load their care plans.
  useEffect(() => {
    if (!selectedPatient) return
    api
      .patientCarePlans(selectedPatient.id)
      .then((plans) => {
        setCarePlans(plans)
        setSelectedPlan(plans[0] ?? null)
      })
      .catch((e) => setError(String(e)))
  }, [selectedPatient])

  // When a care plan is selected, load its tasks.
  useEffect(() => {
    if (!selectedPlan) {
      setTasks([])
      return
    }
    api.carePlanTasks(selectedPlan.id).then(setTasks).catch((e) => setError(String(e)))
  }, [selectedPlan])

  function refreshStats() {
    api.stats().then(setStats).catch(() => {})
  }

  async function handleAdvance(task: Task) {
    try {
      const updated = await api.updateTaskStatus(task.id, NEXT_STATUS[task.status])
      setTasks((prev) => prev.map((t) => (t.id === updated.id ? updated : t)))
      refreshStats()
    } catch (e) {
      setError(String(e))
    }
  }

  return (
    <div className="app">
      <header className="topbar">
        <div className="brand">
          <span className="logo">🏥</span>
          <div>
            <h1>CareBridge</h1>
            <p className="tagline">AI-assisted patient care coordination</p>
          </div>
        </div>
        {stats && (
          <div className="stats">
            <Stat label="Patients" value={stats.patients} />
            <Stat label="Care Plans" value={stats.care_plans} />
            <Stat label="Open Tasks" value={stats.open_tasks} />
          </div>
        )}
      </header>

      {error && <div className="error-banner">⚠️ {error} — is the API running on :8000?</div>}

      <main className="layout">
        <aside className="sidebar">
          <h2>Patients</h2>
          <PatientList
            patients={patients}
            selectedId={selectedPatient?.id ?? null}
            onSelect={setSelectedPatient}
          />
        </aside>

        <section className="content">
          {selectedPatient ? (
            <>
              <div className="content-head">
                <h2>{selectedPatient.full_name}</h2>
                <span className="condition">{selectedPatient.primary_condition}</span>
              </div>

              {carePlans.length > 0 && (
                <div className="plan-tabs">
                  {carePlans.map((plan) => (
                    <button
                      key={plan.id}
                      className={`plan-tab ${plan.id === selectedPlan?.id ? 'active' : ''}`}
                      onClick={() => setSelectedPlan(plan)}
                    >
                      {plan.title}
                    </button>
                  ))}
                </div>
              )}

              {selectedPlan ? (
                <>
                  {selectedPlan.goal && <p className="goal">🎯 {selectedPlan.goal}</p>}
                  <CarePlanBoard tasks={tasks} onAdvance={handleAdvance} />
                  <p className="hint">Tip: click a task card to advance its status.</p>
                </>
              ) : (
                <p className="empty">No care plan for this patient yet.</p>
              )}
            </>
          ) : (
            <p className="empty">Select a patient to view their care plan.</p>
          )}
        </section>
      </main>
    </div>
  )
}

function Stat({ label, value }: { label: string; value: number }) {
  return (
    <div className="stat">
      <span className="stat-value">{value}</span>
      <span className="stat-label">{label}</span>
    </div>
  )
}
