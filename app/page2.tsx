'use client'

import { useMemo, useState } from 'react'
import {
  Activity,
  AlertTriangle,
  ArrowUpRight,
  BarChart3,
  CalendarDays,
  Check,
  ChevronDown,
  CircleHelp,
  Cloud,
  Crosshair,
  Gauge,
  Info,
  Layers3,
  Menu,
  Moon,
  MoreHorizontal,
  Orbit,
  PanelLeftClose,
  Play,
  Plus,
  Radio,
  Search,
  Settings2,
  Sparkles,
  Star,
  Telescope,
  X,
} from 'lucide-react'
import { Button } from '@/components/ui/button'

type View = 'Dashboard' | 'Observation Planner' | 'Sky Report'

const navItems: { label: View; icon: typeof Activity }[] = [
  { label: 'Dashboard', icon: Activity },
  { label: 'Observation Planner', icon: Telescope },
  { label: 'Sky Report', icon: BarChart3 },
]

const targets = [
  { name: 'M31 Andromeda Galaxy', type: 'Galaxy', altitude: '72°', window: '21:40 – 03:10', score: 94, color: 'cyan' },
  { name: 'NGC 7000 North America', type: 'Nebula', altitude: '58°', window: '22:20 – 01:45', score: 88, color: 'amber' },
  { name: 'Jupiter', type: 'Planet', altitude: '41°', window: '23:10 – 02:30', score: 81, color: 'violet' },
]

const chartBars = [42, 58, 76, 64, 91, 73, 48, 66, 84, 62, 78, 55, 70, 89, 61, 47, 72, 93, 69, 80]

export default function Page({ initialView = 'Dashboard' }: { initialView?: View }) {
  const [activeView, setActiveView] = useState<View>(initialView)
  const [sidebarOpen, setSidebarOpen] = useState(false)
  const [sidebarCollapsed, setSidebarCollapsed] = useState(false)
  const [location, setLocation] = useState('Joshua Tree, CA')
  const [isAnalyzing, setIsAnalyzing] = useState(false)
  const [analyzed, setAnalyzed] = useState(false)

  const greeting = useMemo(() => {
    if (activeView === 'Observation Planner') return 'Observation Planner'
    if (activeView === 'Sky Report') return 'Sky Report'
    return 'Good evening, Alex'
  }, [activeView])

  function runAnalysis() {
    setIsAnalyzing(true)
    setTimeout(() => {
      setIsAnalyzing(false)
      setAnalyzed(true)
    }, 850)
  }

  return (
    <main className="min-h-screen bg-background text-foreground">
      <div className="star-field" aria-hidden="true" />
      <div className="relative flex min-h-screen">
        {sidebarOpen && <button className="fixed inset-0 z-30 bg-background/70 backdrop-blur-sm md:hidden" aria-label="Close navigation" onClick={() => setSidebarOpen(false)} />}
        <aside className={`fixed inset-y-0 left-0 z-40 w-[min(86vw,18rem)] border-r border-border/60 bg-card/95 shadow-2xl backdrop-blur-xl transition-[transform,width] duration-300 md:relative md:z-auto md:shadow-none ${sidebarOpen ? 'translate-x-0' : '-translate-x-full md:translate-x-0'} ${sidebarCollapsed ? 'md:w-[72px] md:overflow-hidden' : 'md:w-64'}`}>
          <div className="flex h-full min-h-screen flex-col gap-6 p-4 md:gap-8 md:p-5">
            <div className={`flex items-center gap-3 px-1 ${sidebarCollapsed ? 'md:justify-center' : ''}`}>
              <div className="flex size-9 items-center justify-center rounded-xl bg-primary text-primary-foreground shadow-[0_0_24px_oklch(0.8_0.16_190/0.2)]"><Orbit className="size-5" /></div>
              <div className={`min-w-0 ${sidebarCollapsed ? 'md:hidden' : ''}`}><p className="font-mono text-sm font-bold tracking-[0.18em] text-foreground">ASTROEVENT</p><p className="font-mono text-[10px] tracking-[0.22em] text-primary">AI OBSERVATORY</p></div>
            </div>
            <nav className="flex flex-col gap-1" aria-label="Primary navigation">
              <p className="mb-2 px-3 font-mono text-[10px] uppercase tracking-[0.2em] text-muted-foreground">Workspace</p>
              {navItems.map(({ label, icon: Icon }) => <button key={label} onClick={() => { setActiveView(label); setSidebarOpen(false) }} className={`flex min-h-11 items-center gap-3 rounded-lg px-3 py-2.5 text-left text-sm transition-colors ${activeView === label ? 'bg-primary/12 text-primary' : 'text-muted-foreground hover:bg-accent hover:text-foreground'}`}><Icon className="size-4 shrink-0" /><span className="truncate">{label}</span>{activeView === label && <span className="ml-auto size-1.5 rounded-full bg-primary" />}</button>)}
            </nav>
            <div className="flex flex-col gap-1">
              <p className="mb-2 px-3 font-mono text-[10px] uppercase tracking-[0.2em] text-muted-foreground">Tools</p>
              <button className="flex items-center gap-3 rounded-lg px-3 py-2.5 text-sm text-muted-foreground transition-colors hover:bg-accent hover:text-foreground"><CalendarDays className="size-4" />Planning calendar</button>
              <button className="flex items-center gap-3 rounded-lg px-3 py-2.5 text-sm text-muted-foreground transition-colors hover:bg-accent hover:text-foreground"><Layers3 className="size-4" />My equipment</button>
            </div>
            <div className="mt-auto rounded-xl border border-primary/20 bg-primary/5 p-3"><div className="mb-2 flex items-center justify-between"><span className="font-mono text-[10px] uppercase tracking-[0.16em] text-primary">Pro signal</span><Radio className="size-3.5 text-primary" /></div><p className="text-xs leading-5 text-muted-foreground">AI recommendations are calibrated for your 8-inch Dobsonian.</p></div>
            <div className="flex items-center gap-3 border-t border-border/60 pt-4"><div className="flex size-8 items-center justify-center rounded-full bg-secondary font-mono text-xs text-secondary-foreground">AM</div><div className="min-w-0 flex-1"><p className="truncate text-xs font-medium">Alex Morgan</p><p className="truncate text-[11px] text-muted-foreground">Joshua Tree, CA</p></div><Settings2 className="size-4 text-muted-foreground" /></div>
          </div>
        </aside>

        <section className="min-w-0 flex-1">
          <header className="flex h-16 items-center justify-between border-b border-border/60 px-4 md:px-8">
            <div className="flex min-w-0 items-center gap-2 sm:gap-3"><Button variant="ghost" size="icon" className="shrink-0 md:hidden" onClick={() => setSidebarOpen(true)} aria-label="Open navigation"><Menu className="size-5" /></Button><Button variant="ghost" size="icon" className="hidden shrink-0 md:inline-flex" onClick={() => setSidebarCollapsed(!sidebarCollapsed)} aria-label="Toggle sidebar"><PanelLeftClose className="size-4" /></Button><div className="hidden items-center gap-2 text-xs text-muted-foreground sm:flex"><span>Workspace</span><span>/</span><span className="text-foreground">{activeView}</span></div></div>
            <div className="flex items-center gap-2"><Button variant="outline" size="sm" className="hidden border-border/70 bg-card/40 sm:flex" onClick={() => setLocation(location === 'Joshua Tree, CA' ? 'Big Bear, CA' : 'Joshua Tree, CA')}><Crosshair data-icon="inline-start" />{location}<ChevronDown data-icon="inline-end" /></Button><Button variant="ghost" size="icon" aria-label="Search"><Search className="size-4" /></Button><Button variant="ghost" size="icon" aria-label="Help"><CircleHelp className="size-4" /></Button><div className="ml-1 flex size-8 items-center justify-center rounded-full border border-border bg-secondary font-mono text-[10px]">AM</div></div>
          </header>

          <div className="mx-auto flex max-w-[1500px] flex-col gap-6 p-4 md:p-8">
            <div className="flex flex-col justify-between gap-4 md:flex-row md:items-end"><div><div className="mb-2 flex items-center gap-2"><span className="size-2 animate-pulse rounded-full bg-primary" /><span className="font-mono text-[10px] uppercase tracking-[0.2em] text-primary">Live sky intelligence</span></div><h1 className="text-balance text-3xl font-semibold tracking-tight md:text-4xl">{greeting}</h1><p className="mt-2 max-w-2xl text-sm leading-6 text-muted-foreground">Your next clear window is looking exceptional. Here is what AstroEvent AI found for tonight.</p></div><Button onClick={() => setActiveView('Observation Planner')}><Plus data-icon="inline-start" />New observation</Button></div>

            {activeView === 'Dashboard' && <>
              <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
                {[{ label: 'Sky quality', value: 'Bortle 2', meta: 'Excellent darkness', icon: Star, tone: 'primary' }, { label: 'Cloud cover', value: '4%', meta: 'Clear all night', icon: Cloud, tone: 'cyan' }, { label: 'Seeing', value: '0.82″', meta: 'Above average', icon: Gauge, tone: 'amber' }, { label: 'Moon illumination', value: '12%', meta: 'New moon in 3 days', icon: Moon, tone: 'violet' }].map(({ label, value, meta, icon: Icon }) => <div key={label} className="group rounded-xl border border-border/70 bg-card/75 p-5 backdrop-blur-sm transition-colors hover:border-primary/40"><div className="mb-5 flex items-center justify-between"><span className="text-xs text-muted-foreground">{label}</span><Icon className="size-4 text-primary" /></div><p className="font-mono text-2xl font-medium tracking-tight">{value}</p><p className="mt-1 text-xs text-muted-foreground">{meta}</p></div>)}
              </div>
              <div className="grid gap-4 xl:grid-cols-[1.6fr_1fr]">
                <div className="rounded-xl border border-border/70 bg-card/75 p-5 backdrop-blur-sm"><div className="flex flex-col justify-between gap-3 sm:flex-row sm:items-start"><div><div className="flex items-center gap-2"><Activity className="size-4 text-primary" /><h2 className="font-medium">Tonight&apos;s sky conditions</h2></div><p className="mt-1 text-xs text-muted-foreground">Visibility forecast · {location}</p></div><div className="flex gap-3 font-mono text-[10px] text-muted-foreground"><span className="flex items-center gap-1.5"><span className="size-1.5 rounded-full bg-primary" />Transparency</span><span className="flex items-center gap-1.5"><span className="size-1.5 rounded-full bg-chart-2" />Seeing</span></div></div><div className="relative mt-6 h-48"><div className="absolute inset-0 flex flex-col justify-between text-[10px] text-muted-foreground"><span>Excellent</span><span>Good</span><span>Average</span><span>Poor</span></div><div className="ml-16 flex h-full items-end gap-1.5 border-b border-l border-border/60 px-2 pb-0 pt-3">{chartBars.map((height, i) => <div key={i} className="group relative flex h-full flex-1 items-end"><div className="w-full rounded-t-sm bg-primary/65 transition-all group-hover:bg-primary" style={{ height: `${height}%` }} /><div className="absolute bottom-0 left-1/2 h-1/2 w-0.5 -translate-x-1/2 rounded-full bg-chart-2/70" style={{ height: `${Math.max(12, 100 - height)}%` }} /></div>)}</div><div className="ml-16 flex justify-between px-2 pt-2 font-mono text-[10px] text-muted-foreground"><span>18:00</span><span>21:00</span><span>00:00</span><span>03:00</span><span>06:00</span></div></div></div>
                <div className="rounded-xl border border-primary/25 bg-primary/5 p-5"><div className="flex items-start justify-between"><div><div className="flex items-center gap-2"><Sparkles className="size-4 text-primary" /><h2 className="font-medium">AI brief</h2></div><p className="mt-1 text-xs text-muted-foreground">Generated just now</p></div><Button variant="ghost" size="icon" aria-label="More AI brief options"><MoreHorizontal className="size-4" /></Button></div><div className="mt-6 flex flex-col gap-4"><p className="text-sm leading-6 text-foreground/90">Conditions peak between <strong className="font-mono text-primary">22:10</strong> and <strong className="font-mono text-primary">01:30</strong>. Start with galaxies while the sky is darkest, then switch to Jupiter after midnight.</p><div className="flex items-start gap-3 rounded-lg border border-border/60 bg-card/50 p-3"><AlertTriangle className="mt-0.5 size-4 shrink-0 text-chart-2" /><p className="text-xs leading-5 text-muted-foreground">A light wind shift at 02:00 may affect long-exposure imaging.</p></div><Button variant="outline" size="sm" className="mt-1 w-fit border-primary/30 bg-transparent" onClick={runAnalysis}>{isAnalyzing ? 'Analyzing sky…' : analyzed ? <><Check data-icon="inline-start" />Analysis updated</> : <><Play data-icon="inline-start" />Run deep analysis</>}</Button></div></div>
              </div>
              <div className="rounded-xl border border-border/70 bg-card/75 p-5 backdrop-blur-sm"><div className="mb-5 flex items-center justify-between"><div><h2 className="font-medium">Recommended targets</h2><p className="mt-1 text-xs text-muted-foreground">Selected for your equipment and tonight&apos;s conditions</p></div><Button variant="ghost" size="sm" onClick={() => setActiveView('Observation Planner')}>View planner <ArrowUpRight data-icon="inline-end" /></Button></div><div className="grid gap-3 lg:grid-cols-3">{targets.map((target) => <div key={target.name} className="rounded-lg border border-border/60 bg-background/30 p-4 transition-colors hover:border-primary/40"><div className="flex items-start justify-between gap-3"><div><p className="text-sm font-medium">{target.name}</p><p className="mt-1 text-xs text-muted-foreground">{target.type}</p></div><span className="font-mono text-sm text-primary">{target.score}%</span></div><div className="mt-5 flex items-center justify-between text-xs"><span className="flex items-center gap-1.5 text-muted-foreground"><ArrowUpRight className="size-3" />{target.altitude} max altitude</span><span className="font-mono text-muted-foreground">{target.window}</span></div><div className="mt-3 h-1 overflow-hidden rounded-full bg-secondary"><div className="h-full rounded-full bg-primary" style={{ width: `${target.score}%` }} /></div></div>)}</div></div>
            </>}

            {activeView === 'Observation Planner' && <Planner location={location} />}
            {activeView === 'Sky Report' && <SkyReport analyzed={analyzed} />}
          </div>
        </section>
      </div>
    </main>
  )
}

function Planner({ location }: { location: string }) {
  return <div className="grid gap-4 xl:grid-cols-[1fr_1.4fr]"><div className="rounded-xl border border-border/70 bg-card/75 p-5"><div className="flex items-center gap-2"><Telescope className="size-4 text-primary" /><h2 className="font-medium">Build your session</h2></div><p className="mt-1 text-xs leading-5 text-muted-foreground">AstroEvent will sequence targets around the best altitude, darkness, and seeing.</p><div className="mt-6 flex flex-col gap-4"><label className="flex flex-col gap-2 text-xs text-muted-foreground">Location<select className="rounded-lg border border-border bg-background px-3 py-2.5 text-sm text-foreground outline-none focus:border-primary"><option>{location}</option><option>Big Bear, CA</option><option>Death Valley, CA</option></select></label><label className="flex flex-col gap-2 text-xs text-muted-foreground">Session date<input type="date" defaultValue="2026-09-12" className="rounded-lg border border-border bg-background px-3 py-2.5 text-sm text-foreground outline-none focus:border-primary" /></label><div className="rounded-lg border border-primary/20 bg-primary/5 p-3"><p className="flex items-center gap-2 text-xs font-medium text-primary"><Info className="size-3.5" />AI setup suggestion</p><p className="mt-2 text-xs leading-5 text-muted-foreground">Prioritize deep-sky objects before midnight; moonlight rises after 03:10.</p></div><Button>Generate observation plan <Sparkles data-icon="inline-end" /></Button></div></div><div className="rounded-xl border border-border/70 bg-card/75 p-5"><div className="flex items-center justify-between"><div><h2 className="font-medium">Suggested sequence</h2><p className="mt-1 text-xs text-muted-foreground">3h 50m total · optimized for visual observing</p></div><span className="rounded-full bg-primary/10 px-2.5 py-1 font-mono text-[10px] text-primary">READY</span></div><div className="mt-6 flex flex-col gap-2">{targets.map((target, index) => <div key={target.name} className="flex items-center gap-4 rounded-lg border border-border/60 bg-background/30 p-4"><span className="font-mono text-xs text-muted-foreground">0{index + 1}</span><div className="flex-1"><p className="text-sm font-medium">{target.name}</p><p className="mt-1 text-xs text-muted-foreground">{target.window} · {target.altitude} peak</p></div><span className="font-mono text-xs text-primary">{target.score}% fit</span></div>)}</div></div></div>
}

function SkyReport({ analyzed }: { analyzed: boolean }) {
  return <div className="grid gap-4 lg:grid-cols-[1.5fr_1fr]"><div className="rounded-xl border border-border/70 bg-card/75 p-5"><div className="flex items-center justify-between"><div><div className="flex items-center gap-2"><BarChart3 className="size-4 text-primary" /><h2 className="font-medium">Sky report · September 2026</h2></div><p className="mt-1 text-xs text-muted-foreground">A monthly readout of your observing potential</p></div><Button variant="outline" size="sm">Export report</Button></div><div className="mt-8 grid gap-4 sm:grid-cols-3">{[{ label: 'Clear nights', value: '18', note: '+4 vs August' }, { label: 'Best window', value: 'Sep 12', note: 'Bortle 2 forecast' }, { label: 'Targets visible', value: '126', note: 'Above 30° altitude' }].map((item) => <div key={item.label} className="rounded-lg bg-secondary/50 p-4"><p className="text-xs text-muted-foreground">{item.label}</p><p className="mt-3 font-mono text-2xl text-primary">{item.value}</p><p className="mt-1 text-xs text-muted-foreground">{item.note}</p></div>)}</div><div className="mt-8 rounded-lg border border-border/60 bg-background/20 p-4"><div className="flex items-center justify-between text-xs"><span className="text-muted-foreground">Monthly observing potential</span><span className="font-mono text-primary">82 / 100</span></div><div className="mt-3 h-2 rounded-full bg-secondary"><div className="h-full w-[82%] rounded-full bg-primary" /></div><div className="mt-3 flex justify-between font-mono text-[10px] text-muted-foreground"><span>Sep 01</span><span>Sep 15</span><span>Sep 30</span></div></div></div><div className="rounded-xl border border-primary/25 bg-primary/5 p-5"><div className="flex items-center gap-2"><Sparkles className="size-4 text-primary" /><h2 className="font-medium">Report highlights</h2></div><div className="mt-6 flex flex-col gap-4">{[analyzed ? 'Deep analysis refreshed with the latest forecast.' : 'September opens with a strong deep-sky run.', 'The Andromeda Galaxy reaches its highest altitude on Sep 12.', 'Three new double-star events are visible from your location.'].map((text) => <div key={text} className="flex gap-3 border-b border-border/50 pb-4 last:border-0 last:pb-0"><Check className="mt-0.5 size-4 shrink-0 text-primary" /><p className="text-sm leading-6 text-muted-foreground">{text}</p></div>)}</div></div></div>
}
