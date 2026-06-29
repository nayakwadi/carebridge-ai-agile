import type { Task } from '../api/client'

const priorityClass: Record<Task['priority'], string> = {
  low: 'pri pri-low',
  medium: 'pri pri-medium',
  high: 'pri pri-high',
  urgent: 'pri pri-urgent',
}

interface Props {
  task: Task
  onAdvance: (task: Task) => void
}

export function TaskCard({ task, onAdvance }: Props) {
  return (
    <article className="task-card" onClick={() => onAdvance(task)} title="Click to advance status">
      <div className="task-card-head">
        <span className={priorityClass[task.priority]}>{task.priority}</span>
        {task.due_date && <span className="task-due">due {task.due_date}</span>}
      </div>
      <p className="task-title">{task.title}</p>
    </article>
  )
}
