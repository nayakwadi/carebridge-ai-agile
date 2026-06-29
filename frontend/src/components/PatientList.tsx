import type { Patient } from '../api/client'

interface Props {
  patients: Patient[]
  selectedId: number | null
  onSelect: (patient: Patient) => void
}

export function PatientList({ patients, selectedId, onSelect }: Props) {
  return (
    <ul className="patient-list">
      {patients.map((p) => (
        <li
          key={p.id}
          className={`patient-item ${p.id === selectedId ? 'selected' : ''}`}
          onClick={() => onSelect(p)}
        >
          <div className="patient-row">
            <span className="patient-name">{p.full_name}</span>
            <span className={`risk risk-${p.risk_level}`}>{p.risk_level}</span>
          </div>
          <div className="patient-meta">
            <span>{p.primary_condition}</span>
            <span className="mrn">{p.mrn}</span>
          </div>
        </li>
      ))}
    </ul>
  )
}
