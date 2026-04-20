import { useState } from 'react'
import './App.css'

// ── Field data ────────────────────────────────────────────────────────────────
const ENGINEERING_FIELDS = [
  'Computer Science & IT','Artificial Intelligence & ML','Electronics & Communication',
  'Electrical Engineering','Mechanical Engineering','Civil & Structural Engineering',
  'Robotics & Automation','IoT & Embedded Systems','Cybersecurity',
  'Data Science & Analytics','Chemical Engineering','Biomedical Engineering',
  'Aerospace Engineering','Environmental Engineering','Game Development',
  'AR / VR & Metaverse','Blockchain & Web3','Cloud & DevOps',
  'Automotive & EV Technology','Nanotechnology & Materials',
]
const OTHER_FIELDS = [
  'Healthcare & MedTech','Education & EdTech','Finance & Fintech',
  'Agriculture & AgriTech','Manufacturing & Industry 4.0','Retail & E-Commerce',
  'Sustainability & Clean Energy','Space Technology','Logistics & Supply Chain','Other / Custom',
]
const FIELD_ICONS = {
  'Computer Science & IT':'💻','Artificial Intelligence & ML':'🤖',
  'Electronics & Communication':'📡','Electrical Engineering':'⚡',
  'Mechanical Engineering':'⚙️','Civil & Structural Engineering':'🏗️',
  'Robotics & Automation':'🦾','IoT & Embedded Systems':'📟',
  'Cybersecurity':'🔐','Data Science & Analytics':'📊',
  'Chemical Engineering':'🧪','Biomedical Engineering':'🩺',
  'Aerospace Engineering':'🚀','Environmental Engineering':'🌿',
  'Game Development':'🎮','AR / VR & Metaverse':'🥽',
  'Blockchain & Web3':'🔗','Cloud & DevOps':'☁️',
  'Automotive & EV Technology':'🚗','Nanotechnology & Materials':'⚗️',
  'Healthcare & MedTech':'🏥','Education & EdTech':'📚',
  'Finance & Fintech':'💳','Agriculture & AgriTech':'🌾',
  'Manufacturing & Industry 4.0':'🏭','Retail & E-Commerce':'🛒',
  'Sustainability & Clean Energy':'♻️','Space Technology':'🛸',
  'Logistics & Supply Chain':'📦','Other / Custom':'🔭',
}
const DIFF_COLORS = {
  Beginner:'#22c55e', Intermediate:'#3b82f6', Advanced:'#f97316', Expert:'#ef4444',
}
const SCORE_KEYS = ['feasibility','innovation','risk','impact','complexity']

function money(v) {
  return new Intl.NumberFormat('en-US',{style:'currency',currency:'USD',maximumFractionDigits:0}).format(v)
}

// ── Shared sub-components ─────────────────────────────────────────────────────
function FieldSelector({ field, setField }) {
  return (
    <>
      <label htmlFor="field">Select Your Field</label>
      <select id="field" value={field} onChange={e => setField(e.target.value)}>
        <optgroup label="── Engineering Branches ──">
          {ENGINEERING_FIELDS.map(f => <option key={f} value={f}>{FIELD_ICONS[f]} {f}</option>)}
        </optgroup>
        <optgroup label="── Other Domains ──">
          {OTHER_FIELDS.map(f => <option key={f} value={f}>{FIELD_ICONS[f]} {f}</option>)}
        </optgroup>
      </select>
      <div className="field-badge">
        <span>{FIELD_ICONS[field]}</span><span>{field}</span>
      </div>
    </>
  )
}

function ScoreBar({ label, value, isRisk }) {
  const pct = Math.min(100, Math.round((value / 10) * 100))
  return (
    <div className="score-row">
      <span className="score-label">{label}</span>
      <div className="bar"><div className={`bar-fill${isRisk?' bar-risk':''}`} style={{width:`${pct}%`}} /></div>
      <strong className={isRisk?'risk-num':''}>{value}</strong>
    </div>
  )
}

function Card({ icon, title, children, wide }) {
  return (
    <article className={`card${wide?' card-wide':''}`}>
      <h3>{icon} {title}</h3>
      {children}
    </article>
  )
}

function ComponentExplorer({ components }) {
  const [filter, setFilter] = useState('All')
  if (!components) return null

  const filtered = components.filter(c => {
    if (filter === 'All') return true
    return c.type === filter
  })

  return (
    <div className="comp-explorer">
      <div className="comp-filters">
        {['All', 'Hardware', 'Software'].map(f => (
          <button 
            key={f} 
            className={`filter-btn${filter === f ? ' active' : ''}`}
            onClick={() => setFilter(f)}
          >
            {f}
          </button>
        ))}
      </div>
      <div className="comp-table-wrap">
        <table className="comp-table">
          <thead>
            <tr>
              <th>Type</th>
              <th>Component & Model</th>
              <th>Qty</th>
              <th>Pricing</th>
              <th>Purpose</th>
            </tr>
          </thead>
          <tbody>
            {filtered.map((c, i) => (
              <tr key={i}>
                <td>
                  <span className={`comp-type-tag tag-${(c.type || 'Hardware').toLowerCase()}`}>
                    {c.type || 'Hardware'}
                  </span>
                </td>
                <td>
                  <div className="comp-model">{c.name}</div>
                  <div className="comp-model-sub">{c.model}</div>
                  {c.link_hint && (
                    <a href={`https://${c.link_hint}`} target="_blank" rel="noreferrer" className="comp-link">
                      ↗ {c.link_hint}
                    </a>
                  )}
                </td>
                <td>×{c.qty || 1}</td>
                <td>
                  <div className="comp-total-bold">{money((c.price_usd || 0) * (c.qty || 1))}</div>
                  <div className="comp-price-unit">{money(c.price_usd)} / unit</div>
                </td>
                <td className="comp-purpose">{c.purpose}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}

// ── ANALYZE MODE ──────────────────────────────────────────────────────────────
function AnalyzeMode() {
  const [field, setField] = useState('Computer Science & IT')
  const [idea, setIdea] = useState('')
  const [loading, setLoading] = useState(false)
  const [stage, setStage] = useState('')
  const [error, setError] = useState('')
  const [result, setResult] = useState(null)

  const STAGES = [
    '🔍 Searching internet for components & prices…',
    '🌐 Fetching market data & applications…',
    '🤖 AI analysing with search results…',
    '📊 Building your detailed report…',
  ]

  const onSubmit = async (e) => {
    e.preventDefault()
    setError(''); setResult(null)
    if (idea.trim().length < 20) { setError('Describe your idea in at least 20 characters.'); return }
    setLoading(true)
    let si = 0
    setStage(STAGES[0])
    const interval = setInterval(() => { si = (si+1) % STAGES.length; setStage(STAGES[si]) }, 3500)
    try {
      const res = await fetch('/api/analyze', {
        method:'POST', headers:{'Content-Type':'application/json'},
        body: JSON.stringify({ field, idea }),
      })
      if (!res.ok) { const d = await res.json(); throw new Error(d.detail || 'Analysis failed') }
      setResult(await res.json())
    } catch(err) { setError(err.message) }
    finally { clearInterval(interval); setLoading(false); setStage('') }
  }

  const total = result ? Object.values(result.budget_breakdown_usd||{}).reduce((a,b)=>a+b,0) : 0

  return (
    <div className="layout">
      {/* Input */}
      <section className="panel input-panel">
        <p className="eyebrow">ANALYZE MODE</p>
        <h1>AI Project<br/>Analyzer</h1>
        <p className="intro">
          Describe your idea — the AI searches the internet for real component prices,
          market data, and existing solutions, then gives you a detailed report.
        </p>
        <form onSubmit={onSubmit} className="idea-form">
          <FieldSelector field={field} setField={setField} />
          <label htmlFor="idea">Your Project Idea</label>
          <textarea id="idea" value={idea} onChange={e=>setIdea(e.target.value)} rows={9}
            placeholder={`Describe your ${field} project in detail.\n\nInclude:\n• What problem it solves\n• Who will use it\n• Technologies / hardware needed\n• Scale (local pilot / national / global)\n• Any specific features\n\nMore detail = better & more accurate analysis.`}
          />
          <p className="char-hint">{idea.split(/\s+/).filter(Boolean).length} words — 60+ recommended</p>
          <button type="submit" className="primary-btn" disabled={loading}>
            {loading ? '⏳ Analyzing…' : '⚡ Analyze with AI + Research'}
          </button>
        </form>
        {error && <p className="error">⚠ {error}</p>}
        
        <div className="prompt-template">
          <p className="eyebrow" style={{marginBottom: '0.5rem'}}>💡 Analysis Tip</p>
          <p style={{fontSize: '0.8rem', color: 'var(--text-secondary)', marginBottom: '1rem'}}>
            For the best results, use a structured prompt like this:
          </p>
          <code>{`[PROJECT]: Smart Solar Weeder\n[GOAL]: Reduce herbicide use in organic corn farming by 80%.\n[TECH]: Raspberry Pi 5, YOLOv8, high-torque DC motors.\n[SCALE]: Prototyping for 10-acre local pilots.\n[QUESTION]: What are the exact motor specs and battery requirements for 8h operation?`}</code>
        </div>
      </section>

      {/* Results */}
      <section className="panel result-panel">
        {!result && !loading && (
          <div className="empty">
            <div className="empty-icon">🧠</div>
            <h2>Your AI-Powered Report</h2>
            <p>Powered by <strong>Claude AI + Live Web Search</strong>. Every analysis is unique and based on real internet data.</p>
            <ul className="feature-list">
              <li>⭐ Honest rating & verdict</li>
              <li>✅ Specific pros & cons for YOUR idea</li>
              <li>⚠️ Key technical challenges</li>
              <li>🔩 Real components with <strong>model names & prices</strong></li>
              <li>🛠 Tailored tech stack recommendations</li>
              <li>📈 Market size, growth rate & competitors</li>
              <li>🌍 Real-world applications</li>
              <li>💰 Itemised budget from real prices</li>
              <li>📅 Phase-by-phase development timeline</li>
              <li>💡 Improvement suggestions</li>
              <li>🔗 Similar existing projects</li>
            </ul>
          </div>
        )}
        {loading && (
          <div className="empty loading-state">
            <div className="loader" />
            <h3>{stage}</h3>
            <p className="muted">This usually takes 15–25 seconds</p>
          </div>
        )}
        {result && (
          <div className="results">

            {/* Visual Preview Removed */}

            {/* Header */}
            <header className="summary">
              <div className="summary-top">
                <span className="field-tag">{FIELD_ICONS[result.field]||'🔭'} {result.field}</span>
                <span className="diff-badge" style={{background:DIFF_COLORS[result.difficulty]+'20',color:DIFF_COLORS[result.difficulty],borderColor:DIFF_COLORS[result.difficulty]+'55'}}>
                  {result.difficulty}
                </span>
              </div>
              <h1 className="verdict">{result.verdict}</h1>
              <div className="rating-row">
                <div className="rating-big">{result.rating}<span>/10</span></div>
                <div className="meta-col">
                  <span>💰 {money(result.estimated_budget_usd)} total est.</span>
                  <span>📅 ~{result.estimated_timeline_months} months</span>
                  <span>📈 {result.market_opportunity?.size} market</span>
                </div>
              </div>
              {/* Score bars inside summary for context */}
              <div className="scores" style={{marginTop:'1.5rem',maxWidth:'500px'}}>
                {SCORE_KEYS.map(k => <ScoreBar key={k} label={k} value={result.scores?.[k]??0} isRisk={k==='risk'} />)}
              </div>
            </header>

            <div className="grid">
              <Card icon="🔩" title="Detailed Component Explorer" wide>
                <ComponentExplorer components={result.components_with_specs} />
              </Card>

              <Card icon="✅" title="Core Advantages">
                <ul>{result.pros?.map((p,i)=><li key={i}>{p}</li>)}</ul>
              </Card>

              <Card icon="❌" title="Risks & Cons">
                <ul>{result.cons?.map((c,i)=><li key={i}>{c}</li>)}</ul>
              </Card>

              <Card icon="⚠️" title="Technical Challenges">
                <ul>{result.key_challenges?.map((c,i)=><li key={i}>{c}</li>)}</ul>
              </Card>

              <Card icon="📈" title="Market Opportunity">
                <div className="market-state">
                  <p><strong>Size:</strong> {result.market_opportunity?.size}</p>
                  <p><strong>Growth:</strong> {result.market_opportunity?.growth}</p>
                  <p className="muted" style={{fontSize:'.8rem',marginTop:'.4rem'}}>{result.market_opportunity?.note}</p>
                </div>
                {result.market_opportunity?.competitors?.length>0 && (
                  <div className="pill-row" style={{marginTop:'.8rem'}}>
                    {result.market_opportunity.competitors.map(c=><span key={c} className="pill">{c}</span>)}
                  </div>
                )}
              </Card>

              <Card icon="🛠" title="Recommended Stack">
                <div className="stack-list">
                  {result.suggested_tech_stack?.map((t,i)=>{
                    const [name,...rest] = t.split('—')
                    return (
                      <div key={i} className="stack-item" style={{marginBottom:'.5rem',fontSize:'.88rem'}}>
                        <div style={{fontWeight:700,color:'var(--accent-2)'}}>{name.trim()}</div>
                        {rest.length>0 && <div className="muted" style={{fontSize:'.75rem'}}>{rest.join('—').trim()}</div>}
                      </div>
                    )
                  })}
                </div>
              </Card>

              <Card icon="🌍" title="Applications">
                <ul>{result.real_world_applications?.map((a,i)=><li key={i}>{a}</li>)}</ul>
              </Card>

              <Card icon="💰" title="Detailed Budget" wide>
                <div className="budget-layout">
                  <table className="comp-table">
                    <thead><tr><th>Category</th><th>Estimate</th><th>Allocation</th></tr></thead>
                    <tbody>
                      {Object.entries(result.budget_breakdown_usd||{}).map(([k,v])=>(
                        <tr key={k}>
                          <td style={{fontWeight:600}}>{k}</td>
                          <td className="comp-total-bold">{money(v)}</td>
                          <td>
                            <div className="bar" style={{height:'6px'}}><div className="bar-fill" style={{width:`${Math.round((v/total)*100)}%`}} /></div>
                            <span className="muted" style={{fontSize:'.7rem'}}>{Math.round((v/total)*100)}%</span>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </Card>

              <Card icon="📅" title="Project Timeline">
                <div className="timeline">
                  {Object.entries(result.timeline_phases||{}).map(([phase,months])=>(
                    <div key={phase} className="tl-row" style={{marginBottom:'.8rem'}}>
                      <div style={{fontSize:'.8rem',fontWeight:600,display:'flex',justifyContent:'space-between'}}>
                        <span>{phase}</span>
                        <span className="muted">{months} mo</span>
                      </div>
                      <div className="bar" style={{height:'6px',marginTop:'.3rem'}}>
                        <div className="bar-fill" style={{width:`${Math.round((months/result.estimated_timeline_months)*100)}%`,background:'var(--accent)'}} />
                      </div>
                    </div>
                  ))}
                </div>
              </Card>

              <Card icon="💡" title="Future Improvements">
                <ul>{result.improvement_suggestions?.map((s,i)=><li key={i}>{s}</li>)}</ul>
              </Card>

              {result.industry_news?.length > 0 && (
                <Card icon="📰" title="Industry News & Trends" wide>
                  <div className="news-list" style={{display:'grid',gridTemplateColumns:'repeat(auto-fit, minmax(300px, 1fr))',gap:'1rem'}}>
                    {result.industry_news.map((item, i) => {
                      const match = item.match(/\[(.*?)\]\((.*?)\):(.*)/)
                      if (!match) return null
                      const [_, title, url, body] = match
                      return (
                        <div key={i} className="news-item" style={{background:'rgba(255,255,255,0.03)',padding:'1rem',borderRadius:'8px',border:'1px solid rgba(255,255,255,0.05)'}}>
                          <a href={url} target="_blank" rel="noreferrer" style={{color:'var(--accent)',fontWeight:700,fontSize:'.9rem',display:'block',marginBottom:'.4rem'}}>
                            {title} ↗
                          </a>
                          <p style={{fontSize:'.8rem',lineHeight:1.4}}>{body}</p>
                        </div>
                      )
                    })}
                  </div>
                </Card>
              )}

              {result.research_sources?.length > 0 && (
                <Card icon="📖" title="Research Library" wide>
                  <div className="source-grid" style={{display:'grid',gridTemplateColumns:'repeat(auto-fit, minmax(200px, 1fr))',gap:'.8rem'}}>
                    {result.research_sources.map((item, i) => {
                      const match = item.match(/\[(.*?)\]\((.*?)\)/)
                      if (!match) return null
                      const [_, title, url] = match
                      return (
                        <a key={i} href={url} target="_blank" rel="noreferrer" className="source-link" style={{fontSize:'.8rem',color:'var(--muted)',textDecoration:'none',padding:'.6rem',background:'rgba(255,255,255,0.02)',borderRadius:'4px',display:'block',border:'1px solid rgba(255,255,255,0.03)'}}>
                          📄 {title.slice(0, 50)}...
                        </a>
                      )
                    })}
                  </div>
                </Card>
              )}
            </div>
            <p className="note">⚠ Results are AI-generated from live web search data. Prices and market figures are estimates — verify before committing to a budget.</p>
          </div>
        )}
      </section>
    </div>
  )
}

// ── GENERATE IDEAS MODE ───────────────────────────────────────────────────────
function GenerateMode() {
  const [field, setField] = useState('Computer Science & IT')
  const [context, setContext] = useState('')
  const [loading, setLoading] = useState(false)
  const [stage, setStage] = useState('')
  const [error, setError] = useState('')
  const [result, setResult] = useState(null)
  const [selected, setSelected] = useState(null)

  const STAGES = [
    '🔍 Searching trending topics & problems…',
    '📡 Fetching competition-winning ideas…',
    '🤖 AI generating personalised ideas…',
    '✨ Crafting your idea report…',
  ]

  const onSubmit = async (e) => {
    e.preventDefault()
    setError(''); setResult(null); setSelected(null)
    setLoading(true)
    let si = 0; setStage(STAGES[0])
    const interval = setInterval(() => { si = (si+1)%STAGES.length; setStage(STAGES[si]) }, 3200)
    try {
      const res = await fetch('/api/generate', {
        method:'POST', headers:{'Content-Type':'application/json'},
        body: JSON.stringify({ field, context }),
      })
      if (!res.ok) { const d = await res.json(); throw new Error(d.detail || 'Generation failed') }
      const data = await res.json()
      setResult(data)
    } catch(err) { setError(err.message) }
    finally { clearInterval(interval); setLoading(false); setStage('') }
  }

  return (
    <div className="layout">
      {/* Input */}
      <section className="panel input-panel">
        <p className="eyebrow">GENERATE MODE</p>
        <h1>AI Project<br/>Idea Generator</h1>
        <p className="intro">
          Select your field and the AI will search the internet for current trends,
          unsolved problems, and competition-winning projects — then generate 6 tailored
          project ideas just for you.
        </p>
        <form onSubmit={onSubmit} className="idea-form">
          <FieldSelector field={field} setField={setField} />
          <label htmlFor="context">Your Background (optional)</label>
          <textarea id="context" value={context} onChange={e=>setContext(e.target.value)} rows={4}
            placeholder="e.g. 2nd-year CS student, familiar with Python and React, want to do a final-year project, budget around $200, interested in AI and healthcare…"
          />
          <button type="submit" className="primary-btn" disabled={loading}>
            {loading ? '⏳ Generating…' : '✨ Generate Ideas with AI'}
          </button>
        </form>
        {error && <p className="error">⚠ {error}</p>}
      </section>

      {/* Results */}
      <section className="panel result-panel">
        {!result && !loading && (
          <div className="empty">
            <div className="empty-icon">💡</div>
            <h2>6 AI-Generated Project Ideas</h2>
            <p>The AI will search the internet for current trends and generate 6 unique, detailed project ideas matching your field.</p>
            <ul className="feature-list">
              <li>🌐 Based on <strong>real 2024/2025 trends</strong></li>
              <li>📊 Innovation & feasibility scores</li>
              <li>💰 Realistic budget estimates</li>
              <li>📅 Timeline estimates</li>
              <li>🛠 Key technologies listed</li>
              <li>🧩 Core components with names</li>
              <li>📈 Market need & why it matters</li>
              <li>🏁 Quick-win first milestones</li>
            </ul>
          </div>
        )}
        {loading && (
          <div className="empty loading-state">
            <div className="loader" />
            <h3>{stage}</h3>
            <p className="muted">This usually takes 15–25 seconds</p>
          </div>
        )}
        {result && !selected && (
          <div className="ideas-grid">
            <h2 className="ideas-title">{FIELD_ICONS[result.field]||'💡'} Ideas for <em>{result.field}</em></h2>
            <p className="ideas-sub">Click any idea to see full details</p>
            {result.ideas?.map((idea, i) => (
              <div key={i} className="idea-card" onClick={()=>setSelected(idea)}>
                <div className="idea-card-top">
                  <span className="diff-badge" style={{background:DIFF_COLORS[idea.difficulty]+'20',color:DIFF_COLORS[idea.difficulty],borderColor:DIFF_COLORS[idea.difficulty]+'55'}}>
                    {idea.difficulty}
                  </span>
                  <div className="idea-scores">
                    <span title="Innovation">💡 {idea.innovation_score}</span>
                    <span title="Feasibility">⚙️ {idea.feasibility_score}</span>
                    <span title="Budget">💰 {money(idea.estimated_budget_usd)}</span>
                    <span title="Timeline">📅 {idea.estimated_months}mo</span>
                  </div>
                </div>
                {/* Visual Removed */}
                <h3 className="idea-title">{idea.title}</h3>
                <p className="idea-tagline">{idea.tagline}</p>
                <p className="idea-desc">{idea.description}</p>
                <div className="pill-row">
                  {idea.key_technologies?.slice(0,4).map(t=><span key={t} className="pill">{t}</span>)}
                </div>
                <div className="idea-card-footer">
                  <span>View full details →</span>
                </div>
              </div>
            ))}
          </div>
        )}
        {result && selected && (
          <div className="results">
            <button className="back-btn" onClick={()=>setSelected(null)}>← Back to all ideas</button>
            {/* Visual Preview Removed */}

            <header className="summary">
              <div className="summary-top">
                <span className="diff-badge" style={{background:DIFF_COLORS[selected.difficulty]+'20',color:DIFF_COLORS[selected.difficulty],borderColor:DIFF_COLORS[selected.difficulty]+'55'}}>
                  {selected.difficulty}
                </span>
              </div>
              <h1 className="verdict">{selected.title}</h1>
              <p className="idea-tagline-lg" style={{fontSize:'1.1rem',color:'var(--muted)',marginBottom:'1rem'}}>{selected.tagline}</p>
              <div className="rating-row">
                <div className="meta-col">
                  <span style={{color:'var(--accent-2)'}}>💡 Innovation: {selected.innovation_score}/10</span>
                  <span style={{color:'var(--accent-2)'}}>⚙️ Feasibility: {selected.feasibility_score}/10</span>
                  <span style={{fontWeight:700}}>💰 Budget: {money(selected.estimated_budget_usd)}</span>
                  <span className="muted">📅 Timeline: ~{selected.estimated_months} months</span>
                </div>
              </div>
            </header>

            <div className="grid">
              <Card icon="📝" title="Project Description" wide>
                <p style={{lineHeight:1.6}}>{selected.description}</p>
              </Card>

              {/* Hardware / Software Detail */}
              <Card icon="🔩" title="System Components" wide>
                <div className="comp-explorer">
                  <div className="comp-table-wrap">
                    <table className="comp-table">
                      <thead><tr><th>Component</th><th>Role / Purpose</th></tr></thead>
                      <tbody>
                        {selected.core_components?.map((c,i) => (
                          <tr key={i}>
                            <td style={{fontWeight:600}}>{c}</td>
                            <td className="muted">Primary hardware/module requirement</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              </Card>

              <Card icon="🎯" title="Why it Matters">
                <p style={{fontSize:'.9rem',lineHeight:1.5}}>{selected.why_valuable}</p>
              </Card>

              <Card icon="📈" title="Market Potential">
                <p style={{fontSize:'.9rem',lineHeight:1.5}}>{selected.market_need}</p>
              </Card>

              <Card icon="🛠" title="Key Technologies">
                <div className="pill-row">
                  {selected.key_technologies?.map(t=><span key={t} className="pill">{t}</span>)}
                </div>
              </Card>

              <Card icon="🏁" title="First Milestones">
                <ol className="milestones" style={{paddingLeft:'1.2rem',fontSize:'.9rem'}}>
                  {selected.quick_wins?.map((m,i)=><li key={i} style={{marginBottom:'.4rem'}}>{m}</li>)}
                </ol>
              </Card>
            </div>
            <p className="note">⚠ AI-generated ideas based on live web search. Verify feasibility and market fit before committing.</p>
          </div>
        )}
      </section>
    </div>
  )
}

// ── Root App ──────────────────────────────────────────────────────────────────
export default function App() {
  const [mode, setMode] = useState('analyze')

  return (
    <div className="page">
      <div className="aura aura-one" />
      <div className="aura aura-two" />

      {/* Top nav */}
      <nav className="top-nav">
        <div className="nav-brand">
          <span className="nav-logo">🧠</span>
          <span>AGI Project Analyzer</span>
        </div>
        <div className="mode-toggle">
          <button className={`toggle-btn${mode==='analyze'?' active':''}`} onClick={()=>setMode('analyze')}>
            ⚡ Analyze Idea
          </button>
          <button className={`toggle-btn${mode==='generate'?' active':''}`} onClick={()=>setMode('generate')}>
            💡 Generate Ideas
          </button>
        </div>
      </nav>

      <main className="main-wrap">
        {mode === 'analyze' ? <AnalyzeMode /> : <GenerateMode />}
      </main>
    </div>
  )
}
