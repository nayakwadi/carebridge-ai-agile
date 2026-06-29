import type { Task, TaskStatus } from '../api/client'
import { TaskCard } from './TaskCard'

const COLUMNS: { key: TaskStatus; label: string }[] = [
  { key: 'todo', label: 'To Do' },
  { key: 'in_progress', label: 'In Progress' },
  { key: 'blocked', label: 'Blocked' },
  { key: 'done', label: 'Done' },
]

interface Props {
  tasks: Task[]
  onAdvance: (task: Task) => void
}

export function CarePlanBoard({ tasks, onAdvance }: Props) {
  return (
    <div className="board">
      {COLUMNS.map((col) => {
        const colTasks = tasks.filter((t) => t.status === col.key)
        return (
          <section className="board-col" key={col.key}>
            <header className="board-col-head">
              {col.label} <span className="count">{colTasks.length}</span>
            </header>
            {colTasks.map((t) => (
              <TaskCard key={t.id} task={t} onAdvance={onAdvance} />
            ))}
            {colTasks.length === 0 && <p className="board-empty">—</p>}
          </section>
        )
      })}
    </div>
  )
}
