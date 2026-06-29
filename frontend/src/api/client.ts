const BASE = import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000'

export interface Patient {
  id: number
  mrn: string
  full_name: string
  date_of_birth: string
  primary_condition: string
  risk_level: 'low' | 'medium' | 'high'
  status: string
}

export interface CarePlan {
  id: number
  patient_id: number
  title: string
  goal?: string | null
  status: string
  start_date?: string | null
  target_date?: string | null
}

export type TaskStatus = 'todo' | 'in_progress' | 'blocked' | 'done'

export interface Task {
  id: number
  care_plan_id: number
  title: string
  description?: string | null
  status: TaskStatus
  priority: 'low' | 'medium' | 'high' | 'urgent'
  assignee_id?: number | null
  due_date?: string | null
}

export interface Stats {
  patients: number
  care_plans: number
  open_tasks: number
  cached: boolean
}

async function get<T>(path: string): Promise<T> {
  const res = await fetch(`${BASE}${path}`)
  if (!res.ok) throw new Error(`GET ${path} -> ${res.status}`)
  return (await res.json()) as T
}

export const api = {
  patients: () => get<Patient[]>('/api/patients'),
  patientCarePlans: (id: number) => get<CarePlan[]>(`/api/patients/${id}/care-plans`),
  carePlanTasks: (id: number) => get<Task[]>(`/api/care-plans/${id}/tasks`),
  stats: () => get<Stats>('/api/stats'),
  updateTaskStatus: async (id: number, status: TaskStatus): Promise<Task> => {
    const res = await fetch(`${BASE}/api/tasks/${id}`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ status }),
    })
    if (!res.ok) throw new Error(`PATCH task ${id} -> ${res.status}`)
    return (await res.json()) as Task
  },
}
