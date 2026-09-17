// "use client"

// import { useMemo, useRef, useState } from "react"
// import {
//   Activity,
//   CalendarDays,
//   CheckCircle2,
//   ChevronRight,
//   Cloud,
//   Compass,
//   Crosshair,
//   Eye,
//   Globe2,
//   Loader2,
//   MapPin,
//   Moon,
//   Navigation,
//   Orbit,
//   PanelLeft,
//   Sparkles,
//   Star,
//   Sun,
//   Telescope,
//   Wind,
//   X,
//   Zap,
// } from "lucide-react"

// import { Button } from "@/components/ui/button"

// const API_URL =
//   process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000"

// type LocationData = {
//   name: string
//   latitude: number
//   longitude: number
// }

// type View = "Dashboard" | "Observation Planner" | "Sky Report"

// type PlannerProps = {
//   location: LocationData
//   setLocation: React.Dispatch<React.SetStateAction<LocationData>>
//   observationData: any
//   onAnalysisComplete: (data: any) => void
// }

// const DEFAULT_LOCATION: LocationData = {
//   name: "Pune, Maharashtra, India",
//   latitude: 18.5204,
//   longitude: 73.8567,
// }

// /* =========================================================
//    HELPERS
// ========================================================= */

// function formatValue(value: any, fallback = "—") {
//   if (value === null || value === undefined || value === "") {
//     return fallback
//   }

//   return String(value)
// }

// function getArray(data: any, keys: string[] = []) {
//   if (!data) return []

//   if (Array.isArray(data)) return data

//   for (const key of keys) {
//     if (Array.isArray(data?.[key])) {
//       return data[key]
//     }
//   }

//   return []
// }

// function getNested(data: any, keys: string[]) {
//   let current = data

//   for (const key of keys) {
//     if (current === null || current === undefined) {
//       return null
//     }

//     current = current[key]
//   }

//   return current
// }

// function firstValue(obj: any, keys: string[], fallback: any = null) {
//   for (const key of keys) {
//     if (
//       obj?.[key] !== undefined &&
//       obj?.[key] !== null &&
//       obj?.[key] !== ""
//     ) {
//       return obj[key]
//     }
//   }

//   return fallback
// }

// function normalizeDifficulty(value: any) {
//   if (!value) return "Unknown"

//   if (typeof value === "string") {
//     return value
//       .replaceAll("_", " ")
//       .replace(/\b\w/g, (c) => c.toUpperCase())
//   }

//   if (typeof value === "object") {
//     return (
//       value.label ||
//       value.level ||
//       value.name ||
//       "Unknown"
//     )
//   }

//   return String(value)
// }

// function normalizeVisibility(value: any) {
//   if (typeof value === "boolean") {
//     return value ? "Visible" : "Not visible"
//   }

//   if (!value) return "Unknown"

//   return String(value)
//     .replaceAll("_", " ")
//     .replace(/\b\w/g, (c) => c.toUpperCase())
// }

// function getVisibilityPercentage(object: any) {
//   const value = firstValue(object, [
//     "visibility_percentage",
//     "visibility_percent",
//     "visibility_score",
//     "score",
//     "percentage",
//   ])

//   if (typeof value === "number") {
//     return Math.round(value)
//   }

//   return null
// }

// function getObjectName(object: any) {
//   return firstValue(object, [
//     "name",
//     "object_name",
//     "target_name",
//     "shower_name",
//     "designation",
//   ], "Unknown object")
// }

// function getObjectType(object: any, fallback = "Astronomical Object") {
//   return firstValue(object, [
//     "type",
//     "category",
//     "class",
//     "object_type",
//   ], fallback)
// }

// function getRecommendation(object: any) {
//   return firstValue(object, [
//     "recommendation",
//     "observing_recommendation",
//     "description",
//   ])
// }

// function getRise(object: any) {
//   return firstValue(object, [
//     "rise",
//     "rise_time",
//     "rising",
//     "rise_local",
//   ])
// }

// function getSet(object: any) {
//   return firstValue(object, [
//     "set",
//     "set_time",
//     "setting",
//     "set_local",
//   ])
// }

// function getBestTime(object: any) {
//   return firstValue(object, [
//     "best_time",
//     "best",
//     "best_observation_time",
//     "best_time_local",
//   ])
// }

// function getAzimuth(object: any) {
//   const value = firstValue(object, [
//     "azimuth",
//     "azimuth_deg",
//     "az",
//   ])

//   if (value === null) return null

//   if (typeof value === "number") {
//     return `${Math.round(value)}°`
//   }

//   return String(value)
// }

// function getAltitude(object: any) {
//   const value = firstValue(object, [
//     "altitude",
//     "altitude_deg",
//     "alt",
//   ])

//   if (value === null) return null

//   if (typeof value === "number") {
//     return `${Math.round(value)}°`
//   }

//   return String(value)
// }

// function getDistance(object: any) {
//   return firstValue(object, [
//     "distance",
//     "distance_au",
//     "distance_mly",
//     "distance_km",
//   ])
// }

// function normalizeDistance(value: any) {
//   if (value === null || value === undefined || value === "") {
//     return null
//   }

//   if (typeof value === "number") {
//     return `${value} AU`
//   }

//   return String(value)
// }

// /* =========================================================
//    MAIN APP
// ========================================================= */

// export default function HomePage() {
//   const [activeView, setActiveView] =
//     useState<View>("Observation Planner")

//   const [sidebarOpen, setSidebarOpen] = useState(false)

//   const [location, setLocation] =
//     useState<LocationData>(DEFAULT_LOCATION)

//   const [observationData, setObservationData] =
//     useState<any>(null)

//   return (
//     <div className="min-h-screen bg-[#05070d] text-white">
//       {/* Ambient astronomy background */}
//       <div className="pointer-events-none fixed inset-0 overflow-hidden">
//         <div className="absolute -left-40 top-[-180px] h-[500px] w-[500px] rounded-full bg-cyan-500/10 blur-[130px]" />
//         <div className="absolute right-[-180px] top-[20%] h-[500px] w-[500px] rounded-full bg-violet-600/10 blur-[150px]" />
//         <div className="absolute bottom-[-200px] left-[30%] h-[500px] w-[500px] rounded-full bg-blue-600/10 blur-[150px]" />

//         <div className="absolute inset-0 opacity-[0.035] [background-image:linear-gradient(rgba(255,255,255,.5)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,.5)_1px,transparent_1px)] [background-size:55px_55px]" />
//       </div>

//       <Sidebar
//         activeView={activeView}
//         setActiveView={setActiveView}
//         sidebarOpen={sidebarOpen}
//         setSidebarOpen={setSidebarOpen}
//       />

//       <main className="relative min-h-screen lg:pl-[250px]">
//         {/* Mobile header */}
//         <div className="sticky top-0 z-30 flex h-16 items-center justify-between border-b border-white/10 bg-[#05070d]/90 px-4 backdrop-blur-xl lg:hidden">
//           <button
//             onClick={() => setSidebarOpen(true)}
//             className="rounded-xl border border-white/10 bg-white/[0.04] p-2"
//           >
//             <PanelLeft className="h-5 w-5" />
//           </button>

//           <div className="flex items-center gap-2">
//             <Telescope className="h-5 w-5 text-cyan-300" />
//             <span className="font-semibold">AstroEvent AI</span>
//           </div>

//           <div className="w-9" />
//         </div>

//         <div className="mx-auto max-w-[1550px] px-4 py-6 sm:px-6 lg:px-8 lg:py-8">
//           {activeView === "Observation Planner" && (
//             <Planner
//               location={location}
//               setLocation={setLocation}
//               observationData={observationData}
//               onAnalysisComplete={setObservationData}
//             />
//           )}

//           {activeView === "Dashboard" && (
//             <EmptyView
//               title="Astronomy Dashboard"
//               description="Your observation intelligence dashboard will use the same observation data."
//               icon={<Orbit className="h-8 w-8" />}
//             />
//           )}

//           {activeView === "Sky Report" && (
//             <EmptyView
//               title="Sky Report"
//               description="Detailed sky reports will be generated from your observation session."
//               icon={<Star className="h-8 w-8" />}
//             />
//           )}
//         </div>
//       </main>
//     </div>
//   )
// }

// /* =========================================================
//    SIDEBAR
// ========================================================= */

// function Sidebar({
//   activeView,
//   setActiveView,
//   sidebarOpen,
//   setSidebarOpen,
// }: {
//   activeView: View
//   setActiveView: (view: View) => void
//   sidebarOpen: boolean
//   setSidebarOpen: (value: boolean) => void
// }) {
//   const items: {
//     name: View
//     icon: any
//   }[] = [
//     {
//       name: "Dashboard",
//       icon: Activity,
//     },
//     {
//       name: "Observation Planner",
//       icon: Telescope,
//     },
//     {
//       name: "Sky Report",
//       icon: Star,
//     },
//   ]

//   return (
//     <>
//       {sidebarOpen && (
//         <button
//           aria-label="Close sidebar"
//           onClick={() => setSidebarOpen(false)}
//           className="fixed inset-0 z-40 bg-black/70 lg:hidden"
//         />
//       )}

//       <aside
//         className={`
//           fixed left-0 top-0 z-50 flex h-screen w-[250px]
//           flex-col border-r border-white/10 bg-[#070a12]/95
//           backdrop-blur-2xl transition-transform duration-300
//           lg:translate-x-0
//           ${sidebarOpen ? "translate-x-0" : "-translate-x-full"}
//         `}
//       >
//         <div className="flex h-20 items-center justify-between border-b border-white/10 px-6">
//           <div className="flex items-center gap-3">
//             <div className="relative flex h-10 w-10 items-center justify-center rounded-2xl border border-cyan-400/20 bg-cyan-400/10">
//               <Telescope className="h-5 w-5 text-cyan-300" />
//               <span className="absolute right-1 top-1 h-1.5 w-1.5 rounded-full bg-cyan-300 shadow-[0_0_10px_rgba(103,232,249,.9)]" />
//             </div>

//             <div>
//               <div className="font-semibold tracking-tight">
//                 AstroEvent
//               </div>
//               <div className="text-[10px] uppercase tracking-[0.25em] text-cyan-300/60">
//                 AI Observatory
//               </div>
//             </div>
//           </div>

//           <button
//             onClick={() => setSidebarOpen(false)}
//             className="rounded-lg p-1 text-white/40 hover:bg-white/5 hover:text-white lg:hidden"
//           >
//             <X className="h-5 w-5" />
//           </button>
//         </div>

//         <div className="px-4 py-6">
//           <div className="mb-3 px-3 text-[10px] font-medium uppercase tracking-[0.2em] text-white/30">
//             Observatory
//           </div>

//           <nav className="space-y-1">
//             {items.map((item) => {
//               const Icon = item.icon
//               const active = activeView === item.name

//               return (
//                 <button
//                   key={item.name}
//                   onClick={() => {
//                     setActiveView(item.name)
//                     setSidebarOpen(false)
//                   }}
//                   className={`
//                     group flex w-full items-center gap-3 rounded-xl px-3 py-3
//                     text-left text-sm transition
//                     ${
//                       active
//                         ? "border border-cyan-400/15 bg-cyan-400/10 text-cyan-200"
//                         : "text-white/50 hover:bg-white/[0.04] hover:text-white"
//                     }
//                   `}
//                 >
//                   <Icon
//                     className={`h-4 w-4 ${
//                       active
//                         ? "text-cyan-300"
//                         : "text-white/40 group-hover:text-white"
//                     }`}
//                   />

//                   <span>{item.name}</span>

//                   {active && (
//                     <ChevronRight className="ml-auto h-4 w-4 text-cyan-300/60" />
//                   )}
//                 </button>
//               )
//             })}
//           </nav>
//         </div>

//         <div className="mt-auto p-4">
//           <div className="rounded-2xl border border-white/10 bg-white/[0.025] p-4">
//             <div className="mb-2 flex items-center gap-2">
//               <Sparkles className="h-4 w-4 text-violet-300" />
//               <span className="text-xs font-medium text-white/80">
//                 Astro Intelligence
//               </span>
//             </div>

//             <p className="text-xs leading-5 text-white/35">
//               Astronomy data interpreted by AI for better observation
//               planning.
//             </p>
//           </div>
//         </div>
//       </aside>
//     </>
//   )
// }

// /* =========================================================
//    PLANNER
// ========================================================= */

// function generateTimeOptions() {
//   const options: {
//     value: string
//     label: string
//   }[] = []

//   for (let hour = 0; hour < 24; hour++) {
//     for (let minute = 0; minute < 60; minute += 10) {
//       const value =
//         `${String(hour).padStart(2, "0")}:` +
//         `${String(minute).padStart(2, "0")}`

//       const displayHour = hour % 12 || 12
//       const period = hour < 12 ? "AM" : "PM"

//       const label =
//         `${String(displayHour).padStart(2, "0")}:` +
//         `${String(minute).padStart(2, "0")} ${period}`

//       options.push({
//         value,
//         label,
//       })
//     }
//   }

//   return options
// }

// function Planner({
//   location,
//   setLocation,
//   observationData,
//   onAnalysisComplete,
// }: PlannerProps) {
//   const [fromDate, setFromDate] = useState("")
//   const [toDate, setToDate] = useState("")
//   const [fromTime, setFromTime] = useState("20:00")
//   const [toTime, setToTime] = useState("02:00")

//   const [isAnalyzing, setIsAnalyzing] = useState(false)
//   const [error, setError] = useState("")

//   const [showLocationEditor, setShowLocationEditor] =
//     useState(false)

//   const [manualLocation, setManualLocation] =
//     useState<LocationData>(location)

//   const analyzed = !!observationData


  

//   async function generateObservationPlan() {
//   setError("")

//   if (!fromDate) {
//     setError("Please select a From date.")
//     return
//   }

//   if (!toDate) {
//     setError("Please select a To date.")
//     return
//   }

//   if (!fromTime) {
//     setError("Please select a From time.")
//     return
//   }

//   if (!toTime) {
//     setError("Please select a To time.")
//     return
//   }

//   if (new Date(fromDate) > new Date(toDate)) {
//     setError("To date cannot be earlier than From date.")
//     return
//   }

//   setIsAnalyzing(true)

//   try {
//     const params = new URLSearchParams({
//       latitude: String(location.latitude),
//       longitude: String(location.longitude),
//       from_date: fromDate,
//       to_date: toDate,
//       from_time: fromTime,
//       to_time: toTime,
//     })

//     const response = await fetch(
//       `${API_URL}/api/observation/analyze?${params.toString()}`,
//       {
//         method: "POST",
//         headers: {
//           Accept: "application/json",
//         },
//       }
//     )

//     if (!response.ok) {
//       throw new Error(
//         `Backend returned ${response.status}`
//       )
//     }

//     const data = await response.json()

//     if (data?.success === false) {
//       throw new Error(
//         data?.error || "Observation analysis failed."
//       )
//     }

//     onAnalysisComplete(data)
//   } catch (err: any) {
//     console.error(err)

//     setError(
//       err?.message ||
//         "Unable to connect to AstroEvent AI backend."
//     )
//   } finally {
//     setIsAnalyzing(false)
//   }
// }

//   function useBrowserLocation() {
//     if (!navigator.geolocation) {
//       setError(
//         "Location services are not supported by this browser."
//       )
//       return
//     }

//     navigator.geolocation.getCurrentPosition(
//       (position) => {
//         const nextLocation = {
//           name: "Current Location",
//           latitude: Number(
//             position.coords.latitude.toFixed(6)
//           ),
//           longitude: Number(
//             position.coords.longitude.toFixed(6)
//           ),
//         }

//         setLocation(nextLocation)
//         setManualLocation(nextLocation)
//         setShowLocationEditor(false)
//         setError("")
//       },
//       () => {
//         setError(
//           "Unable to access your current location."
//         )
//       }
//     )
//   }

//   function saveManualLocation() {
//     setLocation({
//       ...manualLocation,
//       latitude: Number(manualLocation.latitude),
//       longitude: Number(manualLocation.longitude),
//     })

//     setShowLocationEditor(false)
//   }

//   return (
//     <div className="space-y-5">
//       {/* =====================================================
//           HEADER
//       ===================================================== */}

//       <div className="relative overflow-hidden rounded-3xl border border-white/10 bg-white/[0.025] p-5 sm:p-7">
//         <div className="absolute right-[-80px] top-[-100px] h-[280px] w-[280px] rounded-full border border-cyan-400/10" />
//         <div className="absolute right-[-30px] top-[-50px] h-[180px] w-[180px] rounded-full border border-violet-400/10" />

//         <div className="relative">
//           <div className="mb-3 flex items-center gap-2 text-xs uppercase tracking-[0.25em] text-cyan-300/60">
//             <Orbit className="h-4 w-4" />
//             Observation Intelligence
//           </div>

//           <div className="flex flex-col justify-between gap-5 lg:flex-row lg:items-end">
//             <div>
//               <h1 className="text-2xl font-semibold tracking-tight sm:text-3xl lg:text-4xl">
//                 Observation Planner
//               </h1>

//               <p className="mt-2 max-w-2xl text-sm leading-6 text-white/40">
//                 Select where and when you want to observe.
//                 AstroEvent AI will analyze the sky, weather and
//                 astronomical targets for your session.
//               </p>
//             </div>

//             <div className="flex items-center gap-2 rounded-full border border-cyan-400/10 bg-cyan-400/[0.04] px-3 py-2 text-xs text-cyan-200/70">
//               <span className="h-2 w-2 rounded-full bg-cyan-300 shadow-[0_0_12px_rgba(103,232,249,.9)]" />
//               Astronomy engine ready
//             </div>
//           </div>
//         </div>
//       </div>

//       {/* =====================================================
//           SESSION SETUP + QUICK SUMMARY
//       ===================================================== */}

//       <div className="grid gap-5 xl:grid-cols-[1.35fr_1fr]">
//         <SessionSetup
//           location={location}
//           fromDate={fromDate}
//           toDate={toDate}
//           fromTime={fromTime}
//           toTime={toTime}
//           setFromDate={setFromDate}
//           setToDate={setToDate}
//           setFromTime={setFromTime}
//           setToTime={setToTime}
//           onChangeLocation={() => {
//             setManualLocation(location)
//             setShowLocationEditor(true)
//           }}
//           onGenerate={generateObservationPlan}
//           isAnalyzing={isAnalyzing}
//         />

//         <QuickSummary
//           observationData={observationData}
//           analyzed={analyzed}
//         />
//       </div>

//       {showLocationEditor && (
//         <LocationEditor
//           location={manualLocation}
//           setLocation={setManualLocation}
//           onClose={() => setShowLocationEditor(false)}
//           onSave={saveManualLocation}
//           onUseCurrent={useBrowserLocation}
//         />
//       )}

//       {error && (
//         <div className="rounded-2xl border border-red-400/20 bg-red-400/[0.06] p-4 text-sm text-red-200">
//           <div className="flex items-start gap-3">
//             <X className="mt-0.5 h-4 w-4 shrink-0" />
//             <div>
//               <div className="font-medium">
//                 Analysis failed
//               </div>
//               <div className="mt-1 text-red-200/60">
//                 {error}
//               </div>
//             </div>
//           </div>
//         </div>
//       )}

//       {/* =====================================================
//           EMPTY STATE
//       ===================================================== */}

//       {!analyzed && !isAnalyzing && (
//         <div className="relative overflow-hidden rounded-3xl border border-white/10 bg-white/[0.02] py-16 text-center">
//           <div className="absolute left-1/2 top-1/2 h-56 w-56 -translate-x-1/2 -translate-y-1/2 rounded-full bg-cyan-400/5 blur-3xl" />

//           <div className="relative mx-auto max-w-lg px-6">
//             <div className="mx-auto mb-5 flex h-16 w-16 items-center justify-center rounded-3xl border border-cyan-400/15 bg-cyan-400/[0.06]">
//               <Telescope className="h-7 w-7 text-cyan-300" />
//             </div>

//             <h2 className="text-xl font-semibold">
//               Ready to explore the sky
//             </h2>

//             <p className="mt-2 text-sm leading-6 text-white/35">
//               Generate an observation plan to discover planets,
//               deep-sky objects, constellations, meteor showers
//               and astronomical events visible during your session.
//             </p>
//           </div>
//         </div>
//       )}

//       {/* =====================================================
//           ANALYZING
//       ===================================================== */}

//       {isAnalyzing && (
//         <div className="rounded-3xl border border-cyan-400/10 bg-cyan-400/[0.025] px-6 py-12 text-center">
//           <Loader2 className="mx-auto h-8 w-8 animate-spin text-cyan-300" />

//           <h2 className="mt-4 text-lg font-semibold">
//             Analyzing your sky...
//           </h2>

//           <p className="mt-2 text-sm text-white/35">
//             Checking weather, Sun, Moon, planets, deep-sky
//             objects, constellations, meteor showers and events.
//           </p>
//         </div>
//       )}

//       {/* =====================================================
//           RESULTS
//       ===================================================== */}

//       {analyzed && !isAnalyzing && (
//         <div className="space-y-5">
//           <div className="grid gap-5 xl:grid-cols-2">
//             <SkyConditions data={observationData} />
//             <SunMoon data={observationData} />

//             <ObjectSection
//               title="Planets"
//               icon={<Orbit className="h-5 w-5" />}
//               description="Planetary targets available during your session"
//               objects={getPlanets(observationData)}
//               empty="No planets meet the selected observation conditions."
//               accent="cyan"
//               fallbackType="Planet"
//             />

//             <ObjectSection
//               title="Deep Sky"
//               icon={<Sparkles className="h-5 w-5" />}
//               description="Galaxies, nebulae and clusters worth observing"
//               objects={getDeepSky(observationData)}
//               empty="No deep-sky targets meet the selected conditions."
//               accent="violet"
//               fallbackType="Deep Sky"
//             />

//             <ObjectSection
//               title="Constellations"
//               icon={<Crosshair className="h-5 w-5" />}
//               description="Constellations visible from your location"
//               objects={getConstellations(observationData)}
//               empty="No constellation data is available."
//               accent="blue"
//               fallbackType="Constellation"
//             />

//             <ObjectSection
//               title="Meteor Showers"
//               icon={<Zap className="h-5 w-5" />}
//               description="Meteor showers active during your selected period"
//               objects={getMeteorShowers(observationData)}
//               empty="No meteor showers are active during this session."
//               accent="amber"
//               fallbackType="Meteor Shower"
//               meteor
//             />
//           </div>

//           <AstronomicalEvents data={observationData} />

//           <AIRecommendation data={observationData} />

//           <ObservationOverview data={observationData} />
//         </div>
//       )}
//     </div>
//   )
// }

// /* =========================================================
//    SESSION SETUP
// ========================================================= */
// function CalendarField({
//   label,
//   value,
//   min,
//   onChange,
// }: {
//   label: string
//   value: string
//   min?: string
//   onChange: (value: string) => void
// }) {
//   const inputRef = useRef<HTMLInputElement>(null)

//   const openCalendar = () => {
//     const input = inputRef.current

//     if (!input) return

//     if ("showPicker" in HTMLInputElement.prototype) {
//       input.showPicker()
//     } else {
//       input.focus()
//     }
//   }

//   return (
//     <label className="block">
//       <div className="mb-2 flex items-center gap-2 text-xs text-white/40">
//         <CalendarDays className="h-4 w-4" />
//         {label}
//       </div>

//       <div
//         onClick={openCalendar}
//         className="relative h-11 w-full cursor-pointer"
//       >
//         <input
//           ref={inputRef}
//           type="date"
//           value={value}
//           min={min}
//           onChange={(e) => onChange(e.target.value)}
//           className="h-11 w-full cursor-pointer rounded-xl border border-white/10 bg-black/20 px-3 pr-10 text-sm text-white outline-none transition focus:border-cyan-400/40 focus:ring-2 focus:ring-cyan-400/10"
//         />

//         <CalendarDays
//           onClick={openCalendar}
//           className="pointer-events-auto absolute right-3 top-1/2 h-4 w-4 -translate-y-1/2 cursor-pointer text-white/50"
//         />
//       </div>
//     </label>
//   )
// }


// function SessionSetup({
//   location,
//   fromDate,
//   toDate,
//   fromTime,
//   toTime,
//   setFromDate,
//   setToDate,
//   setFromTime,
//   setToTime,
//   onChangeLocation,
//   onGenerate,
//   isAnalyzing,
// }: any) {
//   return (
//     <section className="rounded-3xl border border-white/10 bg-white/[0.025] p-5 shadow-2xl shadow-black/20 sm:p-6">
//       <SectionHeader
//         icon={<Navigation className="h-5 w-5" />}
//         eyebrow="Session"
//         title="Observation Setup"
//         description="Define the exact sky window you want AstroEvent AI to analyze."
//       />

//       {/* Location */}
//       <div className="mt-6 rounded-2xl border border-white/10 bg-black/20 p-4">
//         <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
//           <div className="flex min-w-0 items-start gap-3">
//             <div className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-cyan-400/10">
//               <MapPin className="h-5 w-5 text-cyan-300" />
//             </div>

//             <div className="min-w-0">
//               <div className="text-xs uppercase tracking-[0.18em] text-white/30">
//                 Observation Location
//               </div>

//               <div className="mt-1 truncate font-medium">
//                 {location.name}
//               </div>

//               <div className="mt-1 text-xs text-white/35">
//                 {location.latitude.toFixed(4)}°{" "}
//                 {location.latitude >= 0 ? "N" : "S"}
//                 {" · "}
//                 {Math.abs(location.longitude).toFixed(4)}°{" "}
//                 {location.longitude >= 0 ? "E" : "W"}
//               </div>
//             </div>
//           </div>

//           <Button
//             variant="outline"
//             onClick={onChangeLocation}
//             className="shrink-0 border-white/10 bg-white/[0.03] text-white hover:bg-white/[0.07]"
//           >
//             Change location
//           </Button>
//         </div>
//       </div>

//     <div className="mt-5 grid gap-4 sm:grid-cols-2">
//   <CalendarField
//     label="From date"
//     value={fromDate}
//     onChange={(value) => {
//       setFromDate(value)

//       if (toDate && value > toDate) {
//         setToDate("")
//       }
//     }}
//   />

//   <CalendarField
//     label="To date"
//     value={toDate}
//     min={fromDate || undefined}
//     onChange={setToDate}
//   />

//   <TimeSelectField
//     label="From time"
//     icon={<Activity className="h-4 w-4" />}
//     value={fromTime}
//     onChange={setFromTime}
//   />

//   <TimeSelectField
//     label="End time"
//     icon={<Activity className="h-4 w-4" />}
//     value={toTime}
//     onChange={setToTime}
//   />
// </div>  

//       <Button
//         onClick={onGenerate}
//         disabled={isAnalyzing}
//         className="mt-6 h-12 w-full rounded-xl bg-cyan-400 font-semibold text-black hover:bg-cyan-300"
//       >
//         {isAnalyzing ? (
//           <>
//             <Loader2 className="mr-2 h-4 w-4 animate-spin" />
//             Analyzing sky...
//           </>
//         ) : (
//           <>
//             <Sparkles className="mr-2 h-4 w-4" />
//             Generate Observation Plan
//           </>
//         )}
//       </Button>
//     </section>
//   )
// }

// /* =========================================================
//    QUICK SUMMARY
// ========================================================= */

// function QuickSummary({
//   observationData,
//   analyzed,
// }: {
//   observationData: any
//   analyzed: boolean
// }) {
//   const summary = useMemo(() => {
//     if (!observationData) {
//       return {
//         cloud: null,
//         moon: null,
//         targets: null,
//         score: null,
//       }
//     }

//     const cloud =
//       firstValue(observationData, [
//         "cloud_cover",
//       ]) ??
//       getNested(observationData, [
//         "weather",
//         "cloud_cover",
//       ]) ??
//       getNested(observationData, [
//         "weather",
//         "current",
//         "cloud_cover",
//       ])

//     const moon =
//       getNested(observationData, [
//         "moon",
//         "illumination",
//       ]) ??
//       getNested(observationData, [
//         "sun_moon",
//         "moon",
//         "illumination",
//       ])

//     const planets = getPlanets(observationData)
//     const deepSky = getDeepSky(observationData)
//     const constellations = getConstellations(observationData)

//     const targets =
//       planets.length +
//       deepSky.length +
//       constellations.length

//     const score =
//       getNested(observationData, [
//         "ai_recommendation",
//         "score",
//       ]) ??
//       getNested(observationData, [
//         "recommendation",
//         "score",
//       ]) ??
//       observationData?.score

//     return {
//       cloud,
//       moon,
//       targets,
//       score,
//     }
//   }, [observationData])

//   return (
//     <section className="rounded-3xl border border-white/10 bg-white/[0.025] p-5 sm:p-6">
//       <SectionHeader
//         icon={<Activity className="h-5 w-5" />}
//         eyebrow="Overview"
//         title="Quick Summary"
//         description="A fast snapshot of your observing conditions."
//       />

//       <div className="mt-6 grid grid-cols-2 gap-3">
//         <SummaryBox
//           icon={<Cloud className="h-4 w-4" />}
//           label="Cloud Cover"
//           value={
//             summary.cloud !== null
//               ? `${summary.cloud}%`
//               : analyzed
//                 ? "—"
//                 : "—"
//           }
//           accent="cyan"
//         />

//         <SummaryBox
//           icon={<Moon className="h-4 w-4" />}
//           label="Moon"
//           value={
//             summary.moon !== null
//               ? `${summary.moon}%`
//               : "—"
//           }
//           accent="violet"
//         />

//         <SummaryBox
//           icon={<Eye className="h-4 w-4" />}
//           label="Visible Targets"
//           value={
//             summary.targets !== null
//               ? String(summary.targets)
//               : "—"
//           }
//           accent="blue"
//         />

//         <SummaryBox
//           icon={<Sparkles className="h-4 w-4" />}
//           label="Overall Score"
//           value={
//             summary.score !== null
//               ? `${summary.score}/10`
//               : "—"
//           }
//           accent="amber"
//         />
//       </div>
//     </section>
//   )
// }

// /* =========================================================
//    SKY CONDITIONS
// ========================================================= */

// function SkyConditions({ data }: { data: any }) {
//   const weather =
//     data?.weather ||
//     data?.weather_data ||
//     data?.modules?.weather ||
//     {}

//   const hourly = weather?.hourly || {}

//   const cloud = firstValue(
//     weather,
//     ["cloud_cover"]
//   ) ?? firstValue(
//     hourly,
//     ["cloud_cover"]
//   )

//   const humidity = firstValue(
//     weather,
//     ["relative_humidity", "humidity"]
//   ) ?? firstValue(
//     hourly,
//     ["relative_humidity_2m"]
//   )

//   const visibility = firstValue(
//     weather,
//     ["visibility"]
//   ) ?? firstValue(
//     hourly,
//     ["visibility"]
//   )

//   const wind = firstValue(
//     weather,
//     ["wind_speed", "wind_speed_10m"]
//   ) ?? firstValue(
//     hourly,
//     ["wind_speed_10m"]
//   )

//   const temperature = firstValue(
//     weather,
//     ["temperature", "temperature_2m"]
//   ) ?? firstValue(
//     hourly,
//     ["temperature_2m"]
//   )

//   const dewPoint = firstValue(
//     weather,
//     ["dew_point", "dew_point_2m"]
//   ) ?? firstValue(
//     hourly,
//     ["dew_point_2m"]
//   )

//   return (
//     <section className="rounded-3xl border border-white/10 bg-white/[0.025] p-5 sm:p-6">
//       <SectionHeader
//         icon={<Cloud className="h-5 w-5" />}
//         eyebrow="Atmosphere"
//         title="Sky Conditions"
//         description="Weather factors affecting your observation."
//       />

//       <div className="mt-6 grid grid-cols-2 gap-3 sm:grid-cols-3">
//         <Metric
//           label="Cloud"
//           value={cloud !== null ? `${cloud}%` : "—"}
//         />

//         <Metric
//           label="Humidity"
//           value={
//             humidity !== null
//               ? `${humidity}%`
//               : "—"
//           }
//         />

//         <Metric
//           label="Visibility"
//           value={
//             visibility !== null
//               ? `${visibility}`
//               : "—"
//           }
//         />

//         <Metric
//           label="Wind"
//           value={
//             wind !== null
//               ? `${wind}`
//               : "—"
//           }
//         />

//         <Metric
//           label="Temperature"
//           value={
//             temperature !== null
//               ? `${temperature}°`
//               : "—"
//           }
//         />

//         <Metric
//           label="Dew Point"
//           value={
//             dewPoint !== null
//               ? `${dewPoint}°`
//               : "—"
//           }
//         />
//       </div>
//     </section>
//   )
// }

// /* =========================================================
//    SUN & MOON
// ========================================================= */

// function SunMoon({ data }: { data: any }) {
//   const sun =
//     data?.sun ||
//     data?.sun_data ||
//     data?.modules?.sun ||
//     {}

//   const moon =
//     data?.moon ||
//     data?.moon_data ||
//     data?.modules?.moon ||
//     {}

//   const sunrise = firstValue(sun, [
//     "sunrise",
//     "sunrise_local",
//   ])

//   const sunset = firstValue(sun, [
//     "sunset",
//     "sunset_local",
//   ])

//   const astroDusk = firstValue(sun, [
//     "astronomical_dusk",
//     "astronomical_dusk_local",
//     "astronomical_twilight_end",
//   ])

//   const astroDawn = firstValue(sun, [
//     "astronomical_dawn",
//     "astronomical_dawn_local",
//     "astronomical_twilight_start",
//   ])

//   const phase = firstValue(moon, [
//     "phase",
//     "moon_phase",
//   ])

//   const illumination = firstValue(moon, [
//     "illumination",
//     "illumination_percentage",
//   ])

//   const moonrise = firstValue(moon, [
//     "moonrise",
//     "moonrise_local",
//   ])

//   const moonset = firstValue(moon, [
//     "moonset",
//     "moonset_local",
//   ])

//   return (
//     <section className="rounded-3xl border border-white/10 bg-white/[0.025] p-5 sm:p-6">
//       <SectionHeader
//         icon={<Moon className="h-5 w-5" />}
//         eyebrow="Celestial Light"
//         title="Sun & Moon"
//         description="Darkness and lunar conditions during your session."
//       />

//       <div className="mt-6 grid grid-cols-2 gap-3 sm:grid-cols-3">
//         <Metric
//           label="Sunset"
//           value={formatValue(sunset)}
//         />

//         <Metric
//           label="Sunrise"
//           value={formatValue(sunrise)}
//         />

//         <Metric
//           label="Astronomical Dusk"
//           value={formatValue(astroDusk)}
//         />

//         <Metric
//           label="Astronomical Dawn"
//           value={formatValue(astroDawn)}
//         />

//         <Metric
//           label="Moon Phase"
//           value={formatValue(phase)}
//         />

//         <Metric
//           label="Moon Illumination"
//           value={
//             illumination !== null
//               ? `${illumination}%`
//               : "—"
//           }
//         />

//         <Metric
//           label="Moonrise"
//           value={formatValue(moonrise)}
//         />

//         <Metric
//           label="Moonset"
//           value={formatValue(moonset)}
//         />
//       </div>
//     </section>
//   )
// }

// /* =========================================================
//    OBJECT SECTION
// ========================================================= */

// function ObjectSection({
//   title,
//   icon,
//   description,
//   objects,
//   empty,
//   accent,
//   fallbackType,
//   meteor = false,
// }: {
//   title: string
//   icon: React.ReactNode
//   description: string
//   objects: any[]
//   empty: string
//   accent: string
//   fallbackType: string
//   meteor?: boolean
// }) {
//   return (
//     <section className="rounded-3xl border border-white/10 bg-white/[0.025] p-5 sm:p-6">
//       <SectionHeader
//         icon={icon}
//         eyebrow={`${objects.length} target${objects.length === 1 ? "" : "s"}`}
//         title={title}
//         description={description}
//       />

//       {objects.length === 0 ? (
//         <div className="mt-6 rounded-2xl border border-dashed border-white/10 bg-black/10 px-4 py-8 text-center">
//           <div className="text-sm text-white/35">
//             {empty}
//           </div>
//         </div>
//       ) : (
//         <div className="mt-5 grid gap-3">
//           {objects.map((object, index) => (
//             <AstronomyObjectCard
//               key={`${getObjectName(object)}-${index}`}
//               object={object}
//               fallbackType={fallbackType}
//               accent={accent}
//               meteor={meteor}
//             />
//           ))}
//         </div>
//       )}
//     </section>
//   )
// }

// /* =========================================================
//    OBJECT CARD
// ========================================================= */

// function AstronomyObjectCard({
//   object,
//   fallbackType,
//   accent,
//   meteor,
// }: {
//   object: any
//   fallbackType: string
//   accent: string
//   meteor?: boolean
// }) {
//   const name = getObjectName(object)

//   const type = getObjectType(
//     object,
//     fallbackType
//   )

//   const visible =
//     firstValue(object, [
//       "visible",
//       "is_visible",
//       "active",
//     ])

//   const observability = firstValue(object, [
//     "observability",
//     "final_observability",
//     "status",
//   ])

//   const difficulty = normalizeDifficulty(
//     object?.difficulty
//   )

//   const percentage =
//     getVisibilityPercentage(object)

//   const rise = getRise(object)
//   const set = getSet(object)
//   const best = getBestTime(object)
//   const azimuth = getAzimuth(object)
//   const altitude = getAltitude(object)
//   const distance = normalizeDistance(
//     getDistance(object)
//   )

//   const recommendation =
//     getRecommendation(object)

//   return (
//     <div className="group relative overflow-hidden rounded-2xl border border-white/10 bg-black/20 p-4 transition hover:border-white/15 hover:bg-white/[0.035]">
//       <div
//         className={`absolute left-0 top-0 h-full w-[2px] ${
//           accent === "violet"
//             ? "bg-violet-400/70"
//             : accent === "blue"
//               ? "bg-blue-400/70"
//               : accent === "amber"
//                 ? "bg-amber-300/70"
//                 : "bg-cyan-300/70"
//         }`}
//       />

//       {/* Identity */}
//       <div className="flex items-start gap-3">
//         <div className="mt-0.5 flex h-9 w-9 shrink-0 items-center justify-center rounded-xl border border-white/10 bg-white/[0.04]">
//           {meteor ? (
//             <Zap className="h-4 w-4 text-amber-300" />
//           ) : (
//             <Star className="h-4 w-4 text-cyan-300" />
//           )}
//         </div>

//         <div className="min-w-0 flex-1">
//           <div className="flex flex-col gap-2 sm:flex-row sm:items-center sm:justify-between">
//             <div className="min-w-0">
//               <h3 className="truncate text-sm font-semibold text-white/95">
//                 {name}
//               </h3>

//               <div className="mt-0.5 text-xs text-white/35">
//                 {type}
//                 {object?.constellation
//                   ? ` · ${object.constellation}`
//                   : ""}
//               </div>
//             </div>

//             {percentage !== null && (
//               <div className="shrink-0 text-right">
//                 <div className="text-[10px] uppercase tracking-wider text-white/30">
//                   Visibility
//                 </div>

//                 <div className="text-sm font-semibold text-cyan-200">
//                   {percentage}%
//                 </div>
//               </div>
//             )}
//           </div>

//           {/* Visibility bar */}
//           {percentage !== null && (
//             <div className="mt-3 h-1.5 overflow-hidden rounded-full bg-white/5">
//               <div
//                 className="h-full rounded-full bg-gradient-to-r from-cyan-500/70 to-cyan-200"
//                 style={{
//                   width: `${Math.max(
//                     0,
//                     Math.min(100, percentage)
//                   )}%`,
//                 }}
//               />
//             </div>
//           )}

//           {/* Status */}
//           <div className="mt-3 flex flex-wrap items-center gap-2">
//             {visible !== null &&
//               visible !== undefined && (
//                 <StatusPill
//                   positive={
//                     visible === true ||
//                     String(visible).toLowerCase() ===
//                       "true"
//                   }
//                 >
//                   {normalizeVisibility(visible)}
//                 </StatusPill>
//               )}

//             {observability && (
//               <StatusPill>
//                 {normalizeVisibility(observability)}
//               </StatusPill>
//             )}

//             <StatusPill>
//               Difficulty: {difficulty}
//             </StatusPill>
//           </div>

//           {/* Astronomy information */}
//           <div className="mt-4 border-t border-white/5 pt-3">
//             <div className="flex flex-wrap gap-x-4 gap-y-1.5 text-[11px] text-white/45">
//               {!meteor && rise && (
//                 <span>
//                   <strong className="text-white/65">
//                     Rise
//                   </strong>{" "}
//                   {rise}
//                 </span>
//               )}

//               {!meteor && set && (
//                 <span>
//                   <strong className="text-white/65">
//                     Set
//                   </strong>{" "}
//                   {set}
//                 </span>
//               )}

//               {best && (
//                 <span>
//                   <strong className="text-white/65">
//                     Best
//                   </strong>{" "}
//                   {best}
//                 </span>
//               )}

//               {azimuth && (
//                 <span>
//                   <strong className="text-white/65">
//                     Az
//                   </strong>{" "}
//                   {azimuth}
//                 </span>
//               )}

//               {altitude && (
//                 <span>
//                   <strong className="text-white/65">
//                     Alt
//                   </strong>{" "}
//                   {altitude}
//                 </span>
//               )}

//               {distance && (
//                 <span>
//                   <strong className="text-white/65">
//                     Distance
//                   </strong>{" "}
//                   {distance}
//                 </span>
//               )}
//             </div>
//           </div>

//           {/* Recommendation */}
//           {recommendation && (
//             <div className="mt-3 flex gap-2 text-xs leading-5 text-white/40">
//               <Sparkles className="mt-0.5 h-3.5 w-3.5 shrink-0 text-cyan-300/60" />
//               <span>{recommendation}</span>
//             </div>
//           )}
//         </div>
//       </div>
//     </div>
//   )
// }

// /* =========================================================
//    EVENTS
// ========================================================= */

// function AstronomicalEvents({
//   data,
// }: {
//   data: any
// }) {
//   const events =
//     data?.astronomical_events ||
//     data?.astronomicalEvents ||
//     data?.events ||
//     {}

//   const groups = [
//     {
//       title: "Eclipses",
//       items: getArray(events, ["eclipses"]),
//     },
//     {
//       title: "Conjunctions",
//       items: getArray(events, ["conjunctions"]),
//     },
//     {
//       title: "Oppositions",
//       items: getArray(events, ["oppositions"]),
//     },
//     {
//       title: "Occultations",
//       items: getArray(events, ["occultations"]),
//     },
//   ]

//   const total = groups.reduce(
//     (sum, group) => sum + group.items.length,
//     0
//   )

//   return (
//     <section className="rounded-3xl border border-white/10 bg-white/[0.025] p-5 sm:p-6">
//       <SectionHeader
//         icon={<Zap className="h-5 w-5" />}
//         eyebrow={`${total} event${total === 1 ? "" : "s"}`}
//         title="Astronomical Events"
//         description="Major celestial events occurring during your selected session."
//       />

//       {total === 0 ? (
//         <div className="mt-5 flex items-center gap-3 rounded-2xl border border-white/5 bg-black/15 p-4">
//           <CheckCircle2 className="h-5 w-5 text-cyan-300/70" />

//           <div>
//             <div className="text-sm font-medium">
//               No major events
//             </div>

//             <div className="mt-0.5 text-xs text-white/35">
//               No eclipses, conjunctions, oppositions or
//               occultations were detected in this observation
//               window.
//             </div>
//           </div>
//         </div>
//       ) : (
//         <div className="mt-5 grid gap-3 sm:grid-cols-2">
//           {groups.flatMap((group) =>
//             group.items.map(
//               (event: any, index: number) => (
//                 <div
//                   key={`${group.title}-${index}`}
//                   className="rounded-2xl border border-white/10 bg-black/20 p-4"
//                 >
//                   <div className="text-[10px] uppercase tracking-[0.18em] text-cyan-300/50">
//                     {group.title}
//                   </div>

//                   <div className="mt-2 font-medium">
//                     {getObjectName(event)}
//                   </div>

//                   <div className="mt-2 text-xs text-white/40">
//                     {formatValue(
//                       firstValue(event, [
//                         "date",
//                         "time",
//                         "datetime",
//                       ])
//                     )}
//                   </div>
//                 </div>
//               )
//             )
//           )}
//         </div>
//       )}
//     </section>
//   )
// }

// /* =========================================================
//    AI RECOMMENDATION
// ========================================================= */

// function AIRecommendation({
//   data,
// }: {
//   data: any
// }) {
//   const recommendation =
//     data?.ai_recommendation ||
//     data?.recommendation ||
//     data?.ai ||
//     {}

//   const score = recommendation?.score

//   return (
//     <section className="relative overflow-hidden rounded-3xl border border-violet-400/10 bg-violet-400/[0.035] p-5 sm:p-7">
//       <div className="absolute right-[-100px] top-[-100px] h-[300px] w-[300px] rounded-full bg-violet-500/10 blur-[100px]" />

//       <div className="relative">
//         <div className="flex flex-col gap-5 sm:flex-row sm:items-start sm:justify-between">
//           <div>
//             <div className="flex items-center gap-2 text-xs uppercase tracking-[0.22em] text-violet-300/60">
//               <Sparkles className="h-4 w-4" />
//               Gemini Astronomy Intelligence
//             </div>

//             <h2 className="mt-2 text-xl font-semibold">
//               AI Observation Recommendation
//             </h2>
//           </div>

//           {score !== null &&
//             score !== undefined && (
//               <div className="flex h-16 w-16 shrink-0 flex-col items-center justify-center rounded-2xl border border-violet-300/15 bg-violet-300/[0.06]">
//                 <span className="text-lg font-semibold text-violet-200">
//                   {score}
//                 </span>
//                 <span className="text-[9px] uppercase tracking-wider text-white/30">
//                   / 10
//                 </span>
//               </div>
//             )}
//         </div>

//         {recommendation?.recommendation && (
//           <p className="relative mt-5 max-w-4xl text-sm leading-7 text-white/65">
//             {recommendation.recommendation}
//           </p>
//         )}

//         <div className="relative mt-5 grid gap-3 md:grid-cols-3">
//           {recommendation?.best_time && (
//             <AIInfo
//               label="Best Time"
//               value={recommendation.best_time}
//             />
//           )}

//           {recommendation?.weather_summary && (
//             <AIInfo
//               label="Weather"
//               value={recommendation.weather_summary}
//             />
//           )}

//           {recommendation?.astronomy_summary && (
//             <AIInfo
//               label="Astronomy"
//               value={recommendation.astronomy_summary}
//             />
//           )}
//         </div>

//         {Array.isArray(recommendation?.tips) &&
//           recommendation.tips.length > 0 && (
//             <div className="relative mt-5 flex flex-wrap gap-2">
//               {recommendation.tips.map(
//                 (tip: string, index: number) => (
//                   <div
//                     key={index}
//                     className="rounded-full border border-white/10 bg-black/20 px-3 py-1.5 text-xs text-white/45"
//                   >
//                     {tip}
//                   </div>
//                 )
//               )}
//             </div>
//           )}
//       </div>
//     </section>
//   )
// }

// /* =========================================================
//    OBSERVATION OVERVIEW
// ========================================================= */

// function ObservationOverview({
//   data,
// }: {
//   data: any
// }) {
//   const visibility =
//     data?.visibility_summary ||
//     data?.summary?.visibility ||
//     {}

//   const difficulty =
//     data?.difficulty_summary ||
//     data?.summary?.difficulty ||
//     {}

//   return (
//     <section className="grid gap-5 xl:grid-cols-2">
//       <div className="rounded-3xl border border-white/10 bg-white/[0.025] p-5 sm:p-6">
//         <SectionHeader
//           icon={<Eye className="h-5 w-5" />}
//           eyebrow="Targets"
//           title="Visibility Overview"
//           description="How many supplied targets are observable."
//         />

//         <div className="mt-5 space-y-3">
//           <OverviewRow
//             label="Visible"
//             value={
//               firstValue(visibility, [
//                 "visible",
//                 "visible_count",
//               ]) ?? "—"
//             }
//           />

//           <OverviewRow
//             label="Not visible"
//             value={
//               firstValue(visibility, [
//                 "not_visible",
//                 "not_visible_count",
//               ]) ?? "—"
//             }
//           />

//           <OverviewRow
//             label="Total"
//             value={
//               firstValue(visibility, [
//                 "total",
//                 "total_count",
//               ]) ?? "—"
//             }
//           />
//         </div>
//       </div>

//       <div className="rounded-3xl border border-white/10 bg-white/[0.025] p-5 sm:p-6">
//         <SectionHeader
//           icon={<Crosshair className="h-5 w-5" />}
//           eyebrow="Difficulty"
//           title="Observation Difficulty"
//           description="Target difficulty supplied by the astronomy modules."
//         />

//         <div className="mt-5 space-y-3">
//           <OverviewRow
//             label="Easy"
//             value={
//               firstValue(difficulty, [
//                 "easy",
//                 "easy_count",
//               ]) ?? "—"
//             }
//           />

//           <OverviewRow
//             label="Medium"
//             value={
//               firstValue(difficulty, [
//                 "medium",
//                 "medium_count",
//               ]) ?? "—"
//             }
//           />

//           <OverviewRow
//             label="Hard"
//             value={
//               firstValue(difficulty, [
//                 "hard",
//                 "hard_count",
//               ]) ?? "—"
//             }
//           />
//         </div>
//       </div>
//     </section>
//   )
// }

// /* =========================================================
//    LOCATION EDITOR
// ========================================================= */

// function LocationEditor({
//   location,
//   setLocation,
//   onClose,
//   onSave,
//   onUseCurrent,
// }: {
//   location: LocationData
//   setLocation: React.Dispatch<
//     React.SetStateAction<LocationData>
//   >
//   onClose: () => void
//   onSave: () => void
//   onUseCurrent: () => void
// }) {
//   return (
//     <div className="fixed inset-0 z-[100] flex items-center justify-center bg-black/75 p-4 backdrop-blur-sm">
//       <div className="w-full max-w-lg rounded-3xl border border-white/10 bg-[#090c14] p-5 shadow-2xl sm:p-6">
//         <div className="flex items-start justify-between">
//           <div>
//             <div className="flex items-center gap-2 text-xs uppercase tracking-[0.2em] text-cyan-300/60">
//               <MapPin className="h-4 w-4" />
//               Location
//             </div>

//             <h2 className="mt-2 text-xl font-semibold">
//               Choose observation location
//             </h2>
//           </div>

//           <button
//             onClick={onClose}
//             className="rounded-xl p-2 text-white/40 hover:bg-white/5 hover:text-white"
//           >
//             <X className="h-5 w-5" />
//           </button>
//         </div>

//         <button
//           onClick={onUseCurrent}
//           className="mt-6 flex w-full items-center gap-3 rounded-2xl border border-cyan-400/15 bg-cyan-400/[0.05] p-4 text-left hover:bg-cyan-400/[0.08]"
//         >
//           <Navigation className="h-5 w-5 text-cyan-300" />

//           <div>
//             <div className="text-sm font-medium">
//               Use my current location
//             </div>

//             <div className="mt-1 text-xs text-white/35">
//               Use your device GPS coordinates.
//             </div>
//           </div>
//         </button>

//         <div className="my-5 flex items-center gap-3">
//           <div className="h-px flex-1 bg-white/10" />
//           <span className="text-[10px] uppercase tracking-wider text-white/25">
//             or enter coordinates
//           </span>
//           <div className="h-px flex-1 bg-white/10" />
//         </div>

//         <div className="space-y-4">
//           <InputField
//             label="Location name"
//             value={location.name}
//             onChange={(value) =>
//               setLocation((prev) => ({
//                 ...prev,
//                 name: value,
//               }))
//             }
//           />

//           <div className="grid grid-cols-2 gap-3">
//             <InputField
//               label="Latitude"
//               type="number"
//               step="any"
//               value={location.latitude}
//               onChange={(value) =>
//                 setLocation((prev) => ({
//                   ...prev,
//                   latitude: Number(value),
//                 }))
//               }
//             />

//             <InputField
//               label="Longitude"
//               type="number"
//               step="any"
//               value={location.longitude}
//               onChange={(value) =>
//                 setLocation((prev) => ({
//                   ...prev,
//                   longitude: Number(value),
//                 }))
//               }
//             />
//           </div>
//         </div>

//         <div className="mt-6 flex gap-3">
//           <Button
//             variant="outline"
//             onClick={onClose}
//             className="flex-1 border-white/10 bg-white/[0.03]"
//           >
//             Cancel
//           </Button>

//           <Button
//             onClick={onSave}
//             className="flex-1 bg-cyan-400 text-black hover:bg-cyan-300"
//           >
//             Save location
//           </Button>
//         </div>
//       </div>
//     </div>
//   )
// }

// /* =========================================================
//    SMALL COMPONENTS
// ========================================================= */

// function SectionHeader({
//   icon,
//   eyebrow,
//   title,
//   description,
// }: {
//   icon: React.ReactNode
//   eyebrow: string
//   title: string
//   description: string
// }) {
//   return (
//     <div>
//       <div className="flex items-center gap-2 text-[10px] uppercase tracking-[0.2em] text-cyan-300/50">
//         {icon}
//         {eyebrow}
//       </div>

//       <h2 className="mt-2 text-lg font-semibold tracking-tight">
//         {title}
//       </h2>

//       <p className="mt-1 text-xs leading-5 text-white/30">
//         {description}
//       </p>
//     </div>
//   )
// }

// function DateTimeField({
//   label,
//   icon,
//   type,
//   value,
//   min,
//   onChange,
// }: any) {
//   return (
//     <label className="block">
//       <div className="mb-2 flex items-center gap-2 text-xs text-white/40">
//         {icon}
//         {label}
//       </div>

//       <input
//         type={type}
//         value={value}
//         min={min}
//         onChange={(e) => onChange(e.target.value)}
//         className="h-11 w-full rounded-xl border border-white/10 bg-black/20 px-3 text-sm text-white outline-none transition focus:border-cyan-400/40 focus:ring-2 focus:ring-cyan-400/10"
//       />
//     </label>
//   )
// }

// function TimeSelectField({
//   label,
//   icon,
//   value,
//   onChange,
// }: {
//   label: string
//   icon: React.ReactNode
//   value: string
//   onChange: (value: string) => void
// }) {
//   const timeOptions = generateTimeOptions()

//   return (
//     <label className="block">
//       <div className="mb-2 flex items-center gap-2 text-xs text-white/40">
//         {icon}
//         {label}
//       </div>

//       <select
//         value={value}
//         onChange={(e) => onChange(e.target.value)}
//         className="h-11 w-full rounded-xl border border-white/10 bg-black/20 px-3 text-sm text-white outline-none transition focus:border-cyan-400/40 focus:ring-2 focus:ring-cyan-400/10"
//       >
//         {timeOptions.map((time) => (
//           <option
//             key={time.value}
//             value={time.value}
//             className="bg-[#090c14] text-white"
//           >
//             {time.label}
//           </option>
//         ))}
//       </select>
//     </label>
//   )
// }

// function InputField({
//   label,
//   value,
//   onChange,
//   type = "text",
//   step,
// }: any) {
//   return (
//     <label className="block">
//       <div className="mb-2 text-xs text-white/40">
//         {label}
//       </div>

//       <input
//         type={type}
//         step={step}
//         value={value}
//         onChange={(e) => onChange(e.target.value)}
//         className="h-11 w-full rounded-xl border border-white/10 bg-black/20 px-3 text-sm text-white outline-none focus:border-cyan-400/40"
//       />
//     </label>
//   )
// }

// function SummaryBox({
//   icon,
//   label,
//   value,
//   accent,
// }: {
//   icon: React.ReactNode
//   label: string
//   value: string
//   accent: string
// }) {
//   return (
//     <div className="rounded-2xl border border-white/10 bg-black/20 p-4">
//       <div className="flex items-center gap-2 text-xs text-white/35">
//         <span
//           className={
//             accent === "violet"
//               ? "text-violet-300"
//               : accent === "blue"
//                 ? "text-blue-300"
//                 : accent === "amber"
//                   ? "text-amber-300"
//                   : "text-cyan-300"
//           }
//         >
//           {icon}
//         </span>

//         {label}
//       </div>

//       <div className="mt-3 text-2xl font-semibold tracking-tight">
//         {value}
//       </div>
//     </div>
//   )
// }

// function Metric({
//   label,
//   value,
// }: {
//   label: string
//   value: string
// }) {
//   return (
//     <div className="rounded-2xl border border-white/5 bg-black/15 p-3">
//       <div className="text-[10px] uppercase tracking-wider text-white/25">
//         {label}
//       </div>

//       <div className="mt-1.5 truncate text-sm font-medium text-white/80">
//         {value}
//       </div>
//     </div>
//   )
// }

// function StatusPill({
//   children,
//   positive = false,
// }: {
//   children: React.ReactNode
//   positive?: boolean
// }) {
//   return (
//     <span
//       className={`
//         inline-flex items-center gap-1.5 rounded-full border
//         px-2.5 py-1 text-[10px]
//         ${
//           positive
//             ? "border-emerald-400/15 bg-emerald-400/[0.06] text-emerald-300"
//             : "border-white/10 bg-white/[0.025] text-white/45"
//         }
//       `}
//     >
//       {positive && (
//         <span className="h-1.5 w-1.5 rounded-full bg-emerald-300" />
//       )}

//       {children}
//     </span>
//   )
// }

// function AIInfo({
//   label,
//   value,
// }: {
//   label: string
//   value: string
// }) {
//   return (
//     <div className="rounded-2xl border border-white/5 bg-black/15 p-3">
//       <div className="text-[10px] uppercase tracking-wider text-white/25">
//         {label}
//       </div>

//       <div className="mt-1.5 text-xs leading-5 text-white/55">
//         {value}
//       </div>
//     </div>
//   )
// }

// function OverviewRow({
//   label,
//   value,
// }: {
//   label: string
//   value: any
// }) {
//   return (
//     <div className="flex items-center justify-between rounded-xl border border-white/5 bg-black/15 px-4 py-3">
//       <span className="text-xs text-white/40">
//         {label}
//       </span>

//       <span className="text-sm font-medium text-white/75">
//         {value}
//       </span>
//     </div>
//   )
// }

// function EmptyView({
//   title,
//   description,
//   icon,
// }: {
//   title: string
//   description: string
//   icon: React.ReactNode
// }) {
//   return (
//     <div className="flex min-h-[70vh] items-center justify-center">
//       <div className="max-w-lg text-center">
//         <div className="mx-auto flex h-16 w-16 items-center justify-center rounded-3xl border border-cyan-400/10 bg-cyan-400/5 text-cyan-300">
//           {icon}
//         </div>

//         <h1 className="mt-5 text-2xl font-semibold">
//           {title}
//         </h1>

//         <p className="mt-2 text-sm leading-6 text-white/35">
//           {description}
//         </p>
//       </div>
//     </div>
//   )
// }

// /* =========================================================
//    API RESPONSE ADAPTERS
// ========================================================= */

// function getPlanets(data: any) {
//   return getArray(data?.planets, [
//     "objects",
//     "planets",
//   ])
//     .concat(
//       Array.isArray(data?.modules?.planets)
//         ? data.modules.planets
//         : []
//     )
// }

// function getDeepSky(data: any) {
//   return getArray(data?.deep_sky, [
//     "objects",
//     "targets",
//   ])
//     .concat(
//       getArray(data?.deepSky, [
//         "objects",
//         "targets",
//       ])
//     )
// }

// function getConstellations(data: any) {
//   return getArray(data?.constellations, [
//     "objects",
//     "targets",
//   ])
// }

// function getMeteorShowers(data: any) {
//   return getArray(data?.meteor_showers, [
//     "showers",
//     "objects",
//   ])
// }

"use client"

// import { useMemo, useRef, useState } from "react"
import { useEffect, useMemo, useRef, useState } from "react"
import {
  Activity,
  CalendarDays,
  CheckCircle2,
  ChevronRight,
  Cloud,
  Compass,
  Crosshair,
  Eye,
  Globe2,
  Loader2,
  MapPin,
  Moon,
  Navigation,
  Orbit,
  PanelLeft,
  Sparkles,
  Star,
  Sun,
  Telescope,
  Wind,
  X,
  Zap,
  Clock,
} from "lucide-react"

import { Button } from "@/components/ui/button"

const API_URL =
  process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000"

type LocationData = {
  name: string
  latitude: number
  longitude: number
}

// type View = "Dashboard" | "Observation Planner" | "Sky Report"
type View =  "Observation Planner" | "Sky Report"

type PlannerProps = {
  location: LocationData
  setLocation: React.Dispatch<React.SetStateAction<LocationData>>
  observationData: any
  onAnalysisComplete: (data: any) => void
}

const DEFAULT_LOCATION: LocationData = {
  name: "Pune, Maharashtra, India",
  latitude: 18.5204,
  longitude: 73.8567,
}

/* =========================================================
   HELPERS
========================================================= */

// function formatValue(value: any, fallback = "—") {
//   if (value === null || value === undefined || value === "") {
//     return fallback
//   }

//   return String(value)
// }

function formatValue(value: any): string {
  if (
    value === null ||
    value === undefined ||
    value === ""
  ) {
    return "—"
  }

  const text = String(value)

  if (
    text.includes("T") &&
    !Number.isNaN(new Date(text).getTime())
  ) {
    return new Date(text).toLocaleTimeString("en-IN", {
      hour: "numeric",
      minute: "2-digit",
      hour12: true,
    })
  }

  return text
}

function getArray(data: any, keys: string[] = []) {
  if (!data) return []

  if (Array.isArray(data)) return data

  for (const key of keys) {
    if (Array.isArray(data?.[key])) {
      return data[key]
    }
  }

  return []
}

function getNested(data: any, keys: string[]) {
  let current = data

  for (const key of keys) {
    if (current === null || current === undefined) {
      return null
    }

    current = current[key]
  }

  return current
}

function firstValue(obj: any, keys: string[], fallback: any = null) {
  for (const key of keys) {
    if (
      obj?.[key] !== undefined &&
      obj?.[key] !== null &&
      obj?.[key] !== ""
    ) {
      return obj[key]
    }
  }

  return fallback
}

function valueToText(value: any): string | null {
  if (value === null || value === undefined || value === "") return null
  if (typeof value === "string" || typeof value === "number") return String(value)
  if (typeof value === "object") {
    if (typeof value.name === "string") return value.name
    if (typeof value.value === "string") return value.value
    if (typeof value.label === "string") return value.label
  }
  return null
}

function normalizeVisibility(value: any) {
  if (typeof value === "boolean") return value ? "Visible" : "Not visible"
  if (!value) return "Not visible"
  const text = valueToText(value)
  if (!text) return "Not visible"
  return text.replaceAll("_", " ").replace(/\b\w/g, (c) => c.toUpperCase())
}



function getObjectName(object: any): string {
  if (object === null || object === undefined) return "Unknown object"

  // IMPORTANT: Meteor shower name comes directly from API `name`
  if (object?.type === "meteor_shower") {
    return (
      object?.name ||
      object?.shower?.name ||
      object?.meteor_shower?.name ||
      object?.shower_name ||
      "Unknown meteor shower"
    )
  }

  // Sometimes an API returns the object name directly as a string.
  if (typeof object === "string" || typeof object === "number") {
    const text = String(object).trim()
    return text || "Unknown object"
  }

  if (Array.isArray(object)) {
    for (const item of object) {
      const name = getObjectName(item)
      if (name !== "Unknown object") return name
    }
    return "Unknown object"
  }

  const keys = [
    "name",
    "object_name",
    "objectName",
    "target_name",
    "targetName",
    "shower_name",
    "showerName",
    "constellation_name",
    "constellationName",
    "planet_name",
    "planetName",
    "designation",
    "code",
    "id",
    "label",

    "body",
    "planet",
    "target",
    "object",
    "body_name",
    "bodyName",

    "data",
    "result",
    "details",
    "info",
    "metadata",
  ]

  for (const key of keys) {
    const value = object?.[key]

    if (value === null || value === undefined || value === "") continue

    if (typeof value === "string" || typeof value === "number") {
      const text = String(value).trim()
      if (text && !/^\d+$/.test(text)) return text
    }

    if (typeof value === "object") {
      for (const nestedKey of [
        "name",
        "value",
        "label",
        "text",
        "title",
      ]) {
        const nested = value?.[nestedKey]

        if (
          typeof nested === "string" ||
          typeof nested === "number"
        ) {
          const text = String(nested).trim()

          if (text && !/^\d+$/.test(text)) {
            return text
          }
        }
      }

      const nestedName = getObjectName(value)

      if (nestedName !== "Unknown object") {
        return nestedName
      }
    }
  }

  for (const [key, value] of Object.entries(object)) {
    if (typeof value !== "string" && typeof value !== "number") {
      continue
    }

    const text = String(value).trim()

    if (!text || /^\d+$/.test(text)) continue

    const keyText = key.toLowerCase()

    if (
      keyText.includes("name") ||
      keyText.includes("object") ||
      keyText.includes("planet") ||
      keyText.includes("shower") ||
      keyText.includes("constellation") ||
      keyText === "body" ||
      keyText === "target" ||
      keyText === "designation"
    ) {
      return text
    }
  }

  return "Unknown object"
}

function formatObservationTime(value: any) {
  if (!value) return "—"
  const raw = String(value).trim()
  if (/^\d{2}:\d{2}$/.test(raw)) {
    const [hourString, minute] = raw.split(":")
    const hour = Number(hourString)
    const displayHour = hour % 12 || 12
    const period = hour >= 12 ? "PM" : "AM"
    return `${displayHour}:${minute} ${period}`
  }
  const normalized = raw.replace(" ", "T")
  const date = new Date(normalized)
  if (Number.isNaN(date.getTime())) return raw
  return date.toLocaleString("en-IN", {
    day: "2-digit", month: "short", year: "numeric",
    hour: "2-digit", minute: "2-digit", hour12: true,
  })
}

function getAvailability(object: any) {
  const raw = firstValue(object, ["visible", "is_visible"])
  if (typeof raw === "boolean") return raw

  if (typeof raw === "string") {
    const text = raw.toLowerCase().trim()
    if (["true", "visible", "yes", "observable", "available"].includes(text)) return true
    if (["false", "not visible", "not_visible", "no", "below horizon", "below_horizon"].includes(text)) return false
  }

  const observability = firstValue(object, ["observability", "final_observability", "status"])
  if (typeof observability === "string") {
    const text = observability.toLowerCase().trim()
    if (text.includes("visible") || text.includes("observable")) return true
    if (text.includes("not visible") || text.includes("below") || text.includes("unobservable")) return false
  }

  const altitude = firstValue(object, ["altitude", "altitude_deg", "alt"])
  if (typeof altitude === "number") return altitude > 0

  return false
}

function getObjectType(object: any, fallback = "Astronomical Object") {
  return firstValue(object, [
    "type",
    "category",
    "class",
    "object_type",
  ], fallback)
}

function getPeakTime(object: any) {
  return firstValue(object, [
    "peak_time",
    "peakTime",
    "peak_date",
    "peakDate",
    "maximum",
    "max_date",
    "maxDate",
  ])
}

function getPeakRate(object: any) {
  return firstValue(object, [
    "peak_rate",
    "peakRate",
    "zhr",
    "maximum_rate",
    "max_rate",
    "rate",
  ])
}

function getConstellation(object: any) {
  return firstValue(object, [
    "constellation",
    "constellation_name",
    "constellationName",
    "constellation_name_common",
  ])
}

function getRecommendation(object: any) {
  return firstValue(object, [
    "recommendation",
    "observing_recommendation",
    "description",
  ])
}

function getRise(object: any) {
  return firstValue(object, [
    "rise",
    "rise_time",
    "rising",
    "rise_local",
  ])
}

function getSet(object: any) {
  return firstValue(object, [
    "set",
    "set_time",
    "setting",
    "set_local",
  ])
}

// function getBestTime(object: any) {
//   return firstValue(object, [
//     "best_time",
//     "best",
//     "best_observation_time",
//     "best_time_local",
//   ])
// }

function getBestTime(object: any) {
  const best = firstValue(object, [
    "best_time",
    "best",
    "best_observation_time",
    "best_time_local",
  ])

  // If best is already a time string
  if (
    typeof best === "string" ||
    typeof best === "number"
  ) {
    return best
  }

  // If best is an object, extract its time
  if (best && typeof best === "object") {
    return firstValue(best, [
      "time",
      "best_time",
      "best_observation_time",
      "datetime",
      "date",
    ])
  }

  return null
}

function getAzimuth(object: any) {
  const value = firstValue(object, [
    "azimuth",
    "azimuth_deg",
    "az",
  ])

  if (value === null) return null

  if (typeof value === "number") {
    return `${Math.round(value)}°`
  }

  return String(value)
}

function getAltitude(object: any) {
  const value = firstValue(object, [
    "altitude",
    "altitude_deg",
    "alt",
  ])

  if (value === null) return null

  if (typeof value === "number") {
    return `${Math.round(value)}°`
  }

  return String(value)
}

function getDistance(object: any) {
  return firstValue(object, [
    "distance",
    "distance_au",
    "distance_mly",
    "distance_km",
  ])
}

function normalizeDistance(value: any) {
  if (value === null || value === undefined || value === "") {
    return null
  }

  if (typeof value === "number") {
    return `${value} AU`
  }

  return String(value)
}

/* =========================================================
   MAIN APP
========================================================= */

export default function HomePage() {
  const [activeView, setActiveView] =
    useState<View>("Observation Planner")

  const [sidebarOpen, setSidebarOpen] = useState(false)

  const [location, setLocation] =
    useState<LocationData>(DEFAULT_LOCATION)

  const [observationData, setObservationData] =
    useState<any>(null)

  return (
    <div className="min-h-screen bg-[#05070d] text-white">
      {/* Ambient astronomy background */}
      <div className="pointer-events-none fixed inset-0 overflow-hidden">
        <div className="absolute -left-40 top-[-180px] h-[500px] w-[500px] rounded-full bg-cyan-500/10 blur-[130px]" />
        <div className="absolute right-[-180px] top-[20%] h-[500px] w-[500px] rounded-full bg-violet-600/10 blur-[150px]" />
        <div className="absolute bottom-[-200px] left-[30%] h-[500px] w-[500px] rounded-full bg-blue-600/10 blur-[150px]" />

        <div className="absolute inset-0 opacity-[0.035] [background-image:linear-gradient(rgba(255,255,255,.5)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,.5)_1px,transparent_1px)] [background-size:55px_55px]" />
      </div>

      <Sidebar
        activeView={activeView}
        setActiveView={setActiveView}
        sidebarOpen={sidebarOpen}
        setSidebarOpen={setSidebarOpen}
      />

      <main className="relative min-h-screen lg:pl-[250px]">
        {/* Mobile header */}
        <div className="sticky top-0 z-30 flex h-16 items-center justify-between border-b border-white/10 bg-[#05070d]/90 px-4 backdrop-blur-xl lg:hidden">
          <button
            onClick={() => setSidebarOpen(true)}
            className="rounded-xl border border-white/10 bg-white/[0.04] p-2"
          >
            <PanelLeft className="h-5 w-5" />
          </button>

          <div className="flex items-center gap-2">
            <Telescope className="h-5 w-5 text-cyan-300" />
            <span className="font-semibold">AstroEvent AI</span>
          </div>

          <div className="w-9" />
        </div>

        <div className="mx-auto max-w-[1550px] px-4 py-6 sm:px-6 lg:px-8 lg:py-8">
          {activeView === "Observation Planner" && (
            <Planner
              location={location}
              setLocation={setLocation}
              observationData={observationData}
              onAnalysisComplete={setObservationData}
            />
          )}

          {/* {activeView === "Dashboard" && (
            <EmptyView
              title="Astronomy Dashboard"
              description="Your observation intelligence dashboard will use the same observation data."
              icon={<Orbit className="h-8 w-8" />}
            />
          )} */}

          {activeView === "Sky Report" && (
            <EmptyView
              title="Sky Report"
              description="Detailed sky reports will be generated from your observation session."
              icon={<Star className="h-8 w-8" />}
            />
          )}
        </div>
      </main>
    </div>
  )
}

/* =========================================================
   SIDEBAR
========================================================= */

function Sidebar({
  activeView,
  setActiveView,
  sidebarOpen,
  setSidebarOpen,
}: {
  activeView: View
  setActiveView: (view: View) => void
  sidebarOpen: boolean
  setSidebarOpen: (value: boolean) => void
}) {
  const items: {
    name: View
    icon: any
  }[] = [
    // {
    //   name: "Dashboard",
    //   icon: Activity,
    // },
    {
      name: "Observation Planner",
      icon: Telescope,
    },
    // {
    //   name: "Sky Report",
    //   icon: Star,
    // },
  ]

  return (
    <>
      {sidebarOpen && (
        <button
          aria-label="Close sidebar"
          onClick={() => setSidebarOpen(false)}
          className="fixed inset-0 z-40 bg-black/70 lg:hidden"
        />
      )}

      <aside
        className={`
          fixed left-0 top-0 z-50 flex h-screen w-[250px]
          flex-col border-r border-white/10 bg-[#070a12]/95
          backdrop-blur-2xl transition-transform duration-300
          lg:translate-x-0
          ${sidebarOpen ? "translate-x-0" : "-translate-x-full"}
        `}
      >
        <div className="flex h-20 items-center justify-between border-b border-white/10 px-6">
          <div className="flex items-center gap-3">
            <div className="relative flex h-10 w-10 items-center justify-center rounded-2xl border border-cyan-400/20 bg-cyan-400/10">
              <Telescope className="h-5 w-5 text-cyan-300" />
              <span className="absolute right-1 top-1 h-1.5 w-1.5 rounded-full bg-cyan-300 shadow-[0_0_10px_rgba(103,232,249,.9)]" />
            </div>

            <div>
              <div className="font-semibold tracking-tight">
                AstroEvent
              </div>
              <div className="text-[10px] uppercase tracking-[0.25em] text-cyan-300/60">
                AI Observatory
              </div>
            </div>
          </div>

          <button
            onClick={() => setSidebarOpen(false)}
            className="rounded-lg p-1 text-white/40 hover:bg-white/5 hover:text-white lg:hidden"
          >
            <X className="h-5 w-5" />
          </button>
        </div>

        <div className="px-4 py-6">
          <div className="mb-3 px-3 text-[10px] font-medium uppercase tracking-[0.2em] text-white/30">
            Observatory
          </div>

          <nav className="space-y-1">
            {items.map((item) => {
              const Icon = item.icon
              const active = activeView === item.name

              return (
                <button
                  key={item.name}
                  onClick={() => {
                    setActiveView(item.name)
                    setSidebarOpen(false)
                  }}
                  className={`
                    group flex w-full items-center gap-3 rounded-xl px-3 py-3
                    text-left text-sm transition
                    ${
                      active
                        ? "border border-cyan-400/15 bg-cyan-400/10 text-cyan-200"
                        : "text-white/50 hover:bg-white/[0.04] hover:text-white"
                    }
                  `}
                >
                  <Icon
                    className={`h-4 w-4 ${
                      active
                        ? "text-cyan-300"
                        : "text-white/40 group-hover:text-white"
                    }`}
                  />

                  <span>{item.name}</span>

                  {active && (
                    <ChevronRight className="ml-auto h-4 w-4 text-cyan-300/60" />
                  )}
                </button>
              )
            })}
          </nav>
        </div>

        <div className="mt-auto p-4">
          <div className="rounded-2xl border border-white/10 bg-white/[0.025] p-4">
            <div className="mb-2 flex items-center gap-2">
              <Sparkles className="h-4 w-4 text-violet-300" />
              <span className="text-xs font-medium text-white/80">
                Astro Intelligence
              </span>
            </div>

            <p className="text-xs leading-5 text-white/35">
              Astronomy data interpreted by AI for better observation
              planning.
            </p>
          </div>
        </div>
      </aside>
    </>
  )
}

/* =========================================================
   PLANNER
========================================================= */

function generateTimeOptions() {
  const options: {
    value: string
    label: string
  }[] = []

  for (let hour = 0; hour < 24; hour++) {
    for (let minute = 0; minute < 60; minute += 10) {
      const value =
        `${String(hour).padStart(2, "0")}:` +
        `${String(minute).padStart(2, "0")}`

      const displayHour = hour % 12 || 12
      const period = hour < 12 ? "AM" : "PM"

      const label =
        `${String(displayHour).padStart(2, "0")}:` +
        `${String(minute).padStart(2, "0")} ${period}`

      options.push({
        value,
        label,
      })
    }
  }

  return options
}

function Planner({
  location,
  setLocation,
  observationData,
  onAnalysisComplete,
}: PlannerProps) {
  const [fromDate, setFromDate] = useState("")
  const [toDate, setToDate] = useState("")
  const [fromTime, setFromTime] = useState("20:00")
  const [toTime, setToTime] = useState("07:00")

  const [analysisStep, setAnalysisStep] = useState(0)
  const [isAnalyzing, setIsAnalyzing] = useState(false)
  const [typedText, setTypedText] = useState("")
  const [error, setError] = useState("")

  const [showLocationEditor, setShowLocationEditor] =
    useState(false)

  const [manualLocation, setManualLocation] =
    useState<LocationData>(location)

  const analyzed = !!observationData

  useEffect(() => {
    if (!isAnalyzing) {
      setAnalysisStep(0)
      return
    }

    const interval = setInterval(() => {
      setAnalysisStep((prev) => {
        if (prev >= 6) return prev
        return prev + 1
      })
    }, 5000)

    return () => clearInterval(interval)
  }, [isAnalyzing])

  useEffect(() => {
    if (!isAnalyzing) {
      setTypedText("")
      return
    }

    const steps = [
      "Preparing observation location",
      "Checking weather conditions",
      "Calculating Sun & Moon",
      "Finding visible planets",
      "Scanning deep-sky objects",
      "Checking constellations & meteor showers",
      "Checking astronomical events",
    ]

    const text = steps[analysisStep] || ""

    setTypedText("")

    let index = 0

    const typingInterval = setInterval(() => {
      index += 1
      setTypedText(text.slice(0, index))

      if (index >= text.length) {
        clearInterval(typingInterval)
      }
    }, 35)

    return () => clearInterval(typingInterval)
  }, [analysisStep, isAnalyzing])

  async function generateObservationPlan() {
  setError("")

  if (!fromDate) {
    setError("Please select a From date.")
    return
  }

  if (!toDate) {
    setError("Please select a To date.")
    return
  }

  if (!fromTime) {
    setError("Please select a From time.")
    return
  }

  if (!toTime) {
    setError("Please select a To time.")
    return
  }

  if (new Date(fromDate) > new Date(toDate)) {
    setError("To date cannot be earlier than From date.")
    return
  }

  setIsAnalyzing(true)

  try {
    const params = new URLSearchParams({
      latitude: String(location.latitude),
      longitude: String(location.longitude),
      from_date: fromDate,
      to_date: toDate,
      from_time: fromTime,
      to_time: toTime,
    })

    const response = await fetch(
      `${API_URL}/api/observation/analyze?${params.toString()}`,
      {
        method: "POST",
        headers: {
          Accept: "application/json",
        },
      }
    )

    if (!response.ok) {
      throw new Error(
        `Backend returned ${response.status}`
      )
    }

    const data = await response.json()

    if (data?.success === false) {
      throw new Error(
        data?.error || "Observation analysis failed."
      )
    }

    onAnalysisComplete(data)
  } catch (err: any) {
    console.error(err)

    setError(
      err?.message ||
        "Unable to connect to AstroEvent AI backend."
    )
  } finally {
    setIsAnalyzing(false)
  }
}

  function useBrowserLocation() {
  if (!navigator.geolocation) {
    setError(
      "Location services are not supported by this browser."
    )
    return
  }

  navigator.geolocation.getCurrentPosition(
    (position) => {
      const nextLocation = {
        name: "Current Location",
        latitude: Number(
          position.coords.latitude.toFixed(6)
        ),
        longitude: Number(
          position.coords.longitude.toFixed(6)
        ),
      }

      setLocation(nextLocation)
      setManualLocation(nextLocation)
      setShowLocationEditor(false)
      setError("")
    },
    () => {
      setError(
        "Unable to access your current location."
      )
    }
  )
}

  function saveManualLocation() {
    setLocation({
      ...manualLocation,
      latitude: Number(manualLocation.latitude),
      longitude: Number(manualLocation.longitude),
    })

    setShowLocationEditor(false)
  }

  return (
    <div className="space-y-5">
      {/* =====================================================
          HEADER
      ===================================================== */}

      <div className="relative overflow-hidden rounded-3xl border border-white/10 bg-white/[0.025] p-5 sm:p-7">
        <div className="absolute right-[-80px] top-[-100px] h-[280px] w-[280px] rounded-full border border-cyan-400/10" />
        <div className="absolute right-[-30px] top-[-50px] h-[180px] w-[180px] rounded-full border border-violet-400/10" />

        <div className="relative">
          <div className="mb-3 flex items-center gap-2 text-xs uppercase tracking-[0.25em] text-cyan-300/60">
            <Orbit className="h-4 w-4" />
            Observation Intelligence
          </div>

          <div className="flex flex-col justify-between gap-5 lg:flex-row lg:items-end">
            <div>
              <h1 className="text-2xl font-semibold tracking-tight sm:text-3xl lg:text-4xl">
                Observation Planner
              </h1>

              <p className="mt-2 max-w-2xl text-sm leading-6 text-white/40">
                Select where and when you want to observe.
                AstroEvent AI will analyze the sky, weather and
                astronomical targets for your session.
              </p>
            </div>

            <div className="flex items-center gap-2 rounded-full border border-cyan-400/10 bg-cyan-400/[0.04] px-3 py-2 text-xs text-cyan-200/70">
              <span className="h-2 w-2 rounded-full bg-cyan-300 shadow-[0_0_12px_rgba(103,232,249,.9)]" />
              Astronomy engine ready
            </div>
          </div>
        </div>
      </div>

      {/* =====================================================
          SESSION SETUP + QUICK SUMMARY
      ===================================================== */}

      <div className="grid gap-5 xl:grid-cols-[1.35fr_1fr]">
        <SessionSetup
          location={location}
          fromDate={fromDate}
          toDate={toDate}
          fromTime={fromTime}
          toTime={toTime}
          setFromDate={setFromDate}
          setToDate={setToDate}
          setFromTime={setFromTime}
          setToTime={setToTime}
          onChangeLocation={() => {
            setManualLocation(location)
            setShowLocationEditor(true)
          }}
          onGenerate={generateObservationPlan}
          isAnalyzing={isAnalyzing}
        />

        <QuickSummary
          observationData={observationData}
          analyzed={analyzed}
        />
      </div>

      {showLocationEditor && (
        <LocationEditor
          location={manualLocation}
          setLocation={setManualLocation}
          onClose={() => setShowLocationEditor(false)}
          onSave={saveManualLocation}
          onUseCurrent={useBrowserLocation}
        />
      )}

      {error && (
        <div className="rounded-2xl border border-red-400/20 bg-red-400/[0.06] p-4 text-sm text-red-200">
          <div className="flex items-start gap-3">
            <X className="mt-0.5 h-4 w-4 shrink-0" />
            <div>
              <div className="font-medium">
                Analysis failed
              </div>
              <div className="mt-1 text-red-200/60">
                {error}
              </div>
            </div>
          </div>
        </div>
      )}

      {/* =====================================================
          EMPTY STATE
      ===================================================== */}

      {!analyzed && !isAnalyzing && (
        <div className="relative overflow-hidden rounded-3xl border border-white/10 bg-white/[0.02] py-16 text-center">
          <div className="absolute left-1/2 top-1/2 h-56 w-56 -translate-x-1/2 -translate-y-1/2 rounded-full bg-cyan-400/5 blur-3xl" />

          <div className="relative mx-auto max-w-lg px-6">
            <div className="mx-auto mb-5 flex h-16 w-16 items-center justify-center rounded-3xl border border-cyan-400/15 bg-cyan-400/[0.06]">
              <Telescope className="h-7 w-7 text-cyan-300" />
            </div>

            <h2 className="text-xl font-semibold">
              Ready to explore the sky
            </h2>

            <p className="mt-2 text-sm leading-6 text-white/35">
              Generate an observation plan to discover planets,
              deep-sky objects, constellations, meteor showers
              and astronomical events visible during your session.
            </p>
          </div>
        </div>
      )}

      {/* =====================================================
          ANALYZING
      ===================================================== */}

     {/*  {isAnalyzing && (
        <div className="rounded-3xl border border-cyan-400/10 bg-cyan-400/[0.025] px-6 py-12 text-center">
          <Loader2 className="mx-auto h-8 w-8 animate-spin text-cyan-300" />

          <h2 className="mt-4 text-lg font-semibold">
            Analyzing your sky...
          </h2>

          <p className="mt-2 text-sm text-white/35">
            Checking weather, Sun, Moon, planets, deep-sky
            objects, constellations, meteor showers and events.
          </p>
        </div>
      )} */}


    {isAnalyzing && (
  <div className="rounded-3xl border border-cyan-400/10 bg-cyan-400/[0.025] px-6 py-12 text-center">

    {/* Loading Spinner */}
    <Loader2 className="mx-auto h-8 w-8 animate-spin text-cyan-300" />

    {/* Main Heading */}
    <h2 className="mt-4 text-lg font-semibold">
      Analyzing your sky...
    </h2>

    {/* Typewriter Status */}
    <div className="mt-6 flex min-h-[28px] items-center justify-center">

      <div className="text-sm text-white/70">

        {typedText}

        <span className="ml-0.5 inline-block animate-pulse text-cyan-300">
          |
        </span>

      </div>

    </div>

  </div>
)}

      {/* =====================================================
          RESULTS
      ===================================================== */}

      {analyzed && !isAnalyzing && (
        <div className="space-y-5">
          <div className="grid gap-5 xl:grid-cols-2">
            <SkyConditions data={observationData} />
            <SunMoon data={observationData} />

            <ObjectSection
              title="Planets"
              icon={<Orbit className="h-5 w-5" />}
              description="Planetary targets available during your session"
              objects={getPlanets(observationData)}
              empty="No planets meet the selected observation conditions."
              accent="cyan"
              fallbackType="Planet"
            />

            <ObjectSection
              title="Deep Sky"
              icon={<Sparkles className="h-5 w-5" />}
              description="Galaxies, nebulae and clusters worth observing"
              objects={getDeepSky(observationData)}
              empty="No deep-sky targets meet the selected conditions."
              accent="violet"
              fallbackType="Deep Sky"
            />

            <ObjectSection
              title="Constellations"
              icon={<Crosshair className="h-5 w-5" />}
              description="Constellations visible from your location"
              objects={getConstellations(observationData)}
              empty="No constellation data is available."
              accent="blue"
              fallbackType="Constellation"
            />

            <ObjectSection
              title="Meteor Showers"
              icon={<Zap className="h-5 w-5" />}
              description="Meteor showers active during your selected period"
              objects={getMeteorShowers(observationData)}
              empty="No meteor showers are active during this session."
              accent="amber"
              fallbackType="Meteor Shower"
              meteor
            />
          </div>

          <AstronomicalEvents data={observationData} />

          <AIRecommendation data={observationData} />

        </div>
      )}
    </div>
  )
}

/* =========================================================
   SESSION SETUP
========================================================= */
function CalendarField({
  label,
  value,
  min,
  onChange,
}: {
  label: string
  value: string
  min?: string
  onChange: (value: string) => void
}) {
  const inputRef = useRef<HTMLInputElement>(null)

  const openCalendar = () => {
    const input = inputRef.current

    if (!input) return

    if ("showPicker" in HTMLInputElement.prototype) {
      input.showPicker()
    } else {
      input.focus()
    }
  }

  return (
    <label className="block">
      <div className="mb-2 flex items-center gap-2 text-xs text-white/40">
        <CalendarDays className="h-4 w-4" />
        {label}
      </div>

      <div
        onClick={openCalendar}
        className="relative h-11 w-full cursor-pointer"
      >
        <input
          ref={inputRef}
          type="date"
          value={value}
          min={min}
          onChange={(e) => onChange(e.target.value)}
          className="h-11 w-full cursor-pointer rounded-xl border border-white/10 bg-black/20 px-3 pr-10 text-sm text-white outline-none transition focus:border-cyan-400/40 focus:ring-2 focus:ring-cyan-400/10"
        />

        <CalendarDays
          onClick={openCalendar}
          className="pointer-events-auto absolute right-3 top-1/2 h-4 w-4 -translate-y-1/2 cursor-pointer text-white/50"
        />
      </div>
    </label>
  )
}


function SessionSetup({
  location,
  fromDate,
  toDate,
  fromTime,
  toTime,
  setFromDate,
  setToDate,
  setFromTime,
  setToTime,
  onChangeLocation,
  onGenerate,
  isAnalyzing,
}: any) {
  return (
    <section className="rounded-3xl border border-white/10 bg-white/[0.025] p-5 shadow-2xl shadow-black/20 sm:p-6">
      <SectionHeader
        icon={<Navigation className="h-5 w-5" />}
        eyebrow="Session"
        title="Observation Setup"
        description="Define the exact sky window you want AstroEvent AI to analyze."
      />

      {/* Location */}
      <div className="mt-6 rounded-2xl border border-white/10 bg-black/20 p-4">
        <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
          <div className="flex min-w-0 items-start gap-3">
            <div className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-cyan-400/10">
              <MapPin className="h-5 w-5 text-cyan-300" />
            </div>

            <div className="min-w-0">
              <div className="text-xs uppercase tracking-[0.18em] text-white/30">
                Observation Location
              </div>

              <div className="mt-1 truncate font-medium">
                {location.name}
              </div>

              <div className="mt-1 text-xs text-white/35">
                {location.latitude.toFixed(4)}°{" "}
                {location.latitude >= 0 ? "N" : "S"}
                {" · "}
                {Math.abs(location.longitude).toFixed(4)}°{" "}
                {location.longitude >= 0 ? "E" : "W"}
              </div>
            </div>
          </div>

          <Button
            variant="outline"
            onClick={onChangeLocation}
            className="shrink-0 border-white/10 bg-white/[0.03] text-white hover:bg-white/[0.07]"
          >
            Change location
          </Button>
        </div>
      </div>

    <div className="mt-5 grid gap-4 sm:grid-cols-2">
  <CalendarField
    label="From date"
    value={fromDate}
    onChange={(value) => {
      setFromDate(value)

      if (toDate && value > toDate) {
        setToDate("")
      }
    }}
  />

  <CalendarField
    label="To date"
    value={toDate}
    min={fromDate || undefined}
    onChange={setToDate}
  />

  <TimeSelectField
    label="From time"
    icon={<Activity className="h-4 w-4" />}
    value={fromTime}
    onChange={setFromTime}
  />

  <TimeSelectField
    label="End time"
    icon={<Activity className="h-4 w-4" />}
    value={toTime}
    onChange={setToTime}
  />
</div>  

      <Button
        onClick={onGenerate}
        disabled={isAnalyzing}
        className="mt-6 h-12 w-full rounded-xl bg-cyan-400 font-semibold text-black hover:bg-cyan-300"
      >
        {isAnalyzing ? (
          <>
            <Loader2 className="mr-2 h-4 w-4 animate-spin" />
            Analyzing sky...
          </>
        ) : (
          <>
            <Sparkles className="mr-2 h-4 w-4" />
            Generate Observation Plan
          </>
        )}
      </Button>
    </section>
  )
}


function QuickSummary({
  observationData,
  analyzed,
}: {
  observationData: any
  analyzed: boolean
}) {
  const summary = useMemo(() => {
    if (!observationData) {
      return {
        cloud: null,
        moon: null,
        targets: null,
        observationWindow: null,
      }
    }

    // -----------------------------
    // WEATHER / CLOUD COVER
    // -----------------------------
    const weather =
      observationData?.weather ||
      observationData?.weather_data ||
      observationData?.weatherData ||
      observationData

    const hourly =
      weather?.hourly ||
      observationData?.hourly ||
      {}

    const cloudValues = hourly?.cloud_cover

    let cloud: number | null = null

    if (Array.isArray(cloudValues)) {
      const numbers = cloudValues
        .flat(Infinity)
        .map(Number)
        .filter((n) => Number.isFinite(n))

      if (numbers.length > 0) {
        cloud =
          numbers.reduce(
            (sum, number) => sum + number,
            0
          ) / numbers.length
      }
    } else {
      const number = Number(cloudValues)

      if (Number.isFinite(number)) {
        cloud = number
      }
    }

    // -----------------------------
    // MOON
    // -----------------------------
    const sun =
      observationData?.sun ||
      observationData?.sun_data ||
      observationData?.modules?.sun ||
      {}

    const moonValue =
      sun?.moon_illumination ??
      observationData?.moon?.illumination ??
      observationData?.moon?.moon_illumination

    const moon =
      moonValue !== null &&
      moonValue !== undefined &&
      moonValue !== ""
        ? Number(moonValue)
        : null

    // -----------------------------
    // VISIBLE TARGETS
    // -----------------------------
    const planets = getPlanets(observationData)
    const deepSky = getDeepSky(observationData)
    const constellations =
      getConstellations(observationData)

    const targets =
      planets.length +
      deepSky.length +
      constellations.length

    // -----------------------------
    // OBSERVATION WINDOW
    // -----------------------------
    const fromTime =
      getNested(observationData, [
        "observation",
        "from_time",
      ]) ??
      getNested(observationData, [
        "selected",
        "from_time",
      ]) ??
      observationData?.from_time

    const toTime =
      getNested(observationData, [
        "observation",
        "to_time",
      ]) ??
      getNested(observationData, [
        "selected",
        "to_time",
      ]) ??
      observationData?.to_time

    const observationWindow =
      fromTime && toTime
        ? `${fromTime} – ${toTime}`
        : null

    return {
      cloud,
      moon,
      targets,
      observationWindow,
    }
  }, [observationData])

  return (
    <section className="rounded-3xl border border-white/10 bg-white/[0.025] p-5 sm:p-6">
      <SectionHeader
        icon={<Activity className="h-5 w-5" />}
        eyebrow="Overview"
        title="Quick Summary"
        description="A fast snapshot of your observing conditions."
      />

      <div className="mt-6 grid grid-cols-2 gap-3">

        {/* Cloud Cover */}
        <SummaryBox
          icon={<Cloud className="h-4 w-4" />}
          label="Cloud Cover"
          value={
            summary.cloud !== null
              ? `${summary.cloud.toFixed(0)}%`
              : "—"
          }
          accent="cyan"
           labelClassName="text-xs uppercase tracking-wider text-white"
  valueClassName="text-lg font-semibold text-white"
        />

        {/* Moon */}
        <SummaryBox
          icon={<Moon className="h-4 w-4" />}
          label="Moon Illumination"
          value={
            summary.moon !== null &&
            Number.isFinite(summary.moon)
              ? `${summary.moon.toFixed(1)}%`
              : "—"
          }
          accent="violet"
           labelClassName="text-xs uppercase tracking-wider text-white"
  valueClassName="text-lg font-semibold text-white"
        />

        {/* Visible Targets */}
        <SummaryBox
          icon={<Eye className="h-4 w-4" />}
          label="Visible Targets"
          value={
            summary.targets !== null
              ? String(summary.targets)
              : "—"
          }
          accent="blue"
           labelClassName="text-xs uppercase tracking-wider text-white"
  valueClassName="text-lg font-semibold text-white"
        />

        {/* Observation Window */}
        <SummaryBox
          icon={<Clock className="h-4 w-4" />}
          label="Observation Window"
          value={
            summary.observationWindow ?? "—"
          }
          accent="amber"
           labelClassName="text-xs uppercase tracking-wider text-white"
  valueClassName="text-lg font-semibold text-white"
        />

      </div>
    </section>
  )
}

function SkyConditions({ data }: { data: any }) {
  function getAverage(value: any): number | null {
    if (Array.isArray(value)) {
      const numbers = value
        .flat(Infinity)
        .map(Number)
        .filter((n) => Number.isFinite(n))

      if (numbers.length === 0) {
        return null
      }

      return (
        numbers.reduce((sum, number) => sum + number, 0) /
        numbers.length
      )
    }

    if (
      typeof value === "number" ||
      typeof value === "string"
    ) {
      const number = Number(value)

      return Number.isFinite(number) ? number : null
    }

    return null
  }

  /*
   * Open-Meteo data is normally inside:
   *
   * data.weather.hourly
   *
   * But this also checks a few common structures
   * so the component is more tolerant.
   */

  const weather =
    data?.weather ||
    data?.weather_data ||
    data?.weatherData ||
    data

  const hourly =
    weather?.hourly ||
    data?.hourly ||
    {}

  const cloud = hourly?.cloud_cover
  const humidity = hourly?.relative_humidity_2m
  const visibility = hourly?.visibility
  const wind = hourly?.wind_speed_10m
  const temperature = hourly?.temperature_2m
  const dewPoint = hourly?.dew_point_2m

  const cloudAvg = getAverage(cloud)
  const humidityAvg = getAverage(humidity)
  const visibilityAvg = getAverage(visibility)
  const windAvg = getAverage(wind)
  const temperatureAvg = getAverage(temperature)
  const dewPointAvg = getAverage(dewPoint)

  return (
    <section className="rounded-3xl border border-white/10 bg-white/[0.025] p-5 sm:p-6">
      <SectionHeader
        icon={<Cloud className="h-5 w-5" />}
        eyebrow="Atmosphere"
        title="Sky Conditions"
        description="Weather factors affecting your observation."
      />

      <div className="mt-6 grid grid-cols-2 gap-3 sm:grid-cols-3">
        <Metric
          label="Cloud"
          value={
            cloudAvg !== null
              ? `${cloudAvg.toFixed(0)}%`
              : "—"
          }
        />

        <Metric
          label="Humidity"
          value={
            humidityAvg !== null
              ? `${humidityAvg.toFixed(0)}%`
              : "—"
          }
        />

        <Metric
          label="Visibility"
          value={
            visibilityAvg !== null
              ? `${(visibilityAvg / 1000).toFixed(1)} km`
              : "—"
          }
        />

        <Metric
          label="Wind"
          value={
            windAvg !== null
              ? `${windAvg.toFixed(1)} km/h`
              : "—"
          }
        />

        <Metric
          label="Temperature"
          value={
            temperatureAvg !== null
              ? `${temperatureAvg.toFixed(1)}°C`
              : "—"
          }
        />

        <Metric
          label="Dew Point"
          value={
            dewPointAvg !== null
              ? `${dewPointAvg.toFixed(1)}°C`
              : "—"
          }
        />
      </div>
    </section>
  )
}


function SunMoon({ data }: { data: any }) {
  const sun =
    data?.sun ||
    data?.sun_data ||
    data?.modules?.sun ||
    {}

  const moon =
    data?.moon ||
    data?.moon_data ||
    data?.modules?.moon ||
    sun ||
    {}

  const sunset = firstValue(sun, [
    "sunset",
    "sunset_local",
  ])

  const sunrise = firstValue(sun, [
    "sunrise",
    "sunrise_local",
  ])

  

  const astroDusk = firstValue(sun, [
    "astronomical_twilight_end",
    "astronomical_dusk",
    "astronomical_dusk_local",
  ])

  const astroDawn = firstValue(sun, [
    "astronomical_twilight_begin",
    "astronomical_dawn",
    "astronomical_dawn_local",
  ])

  const phase = firstValue(moon, [
    "moon_phase",
    "phase",
  ])

  const illumination = firstValue(moon, [
    "moon_illumination",
    "illumination",
    "illumination_percentage",
  ])

  const moonrise = firstValue(moon, [
    "moonrise",
    "moonrise_local",
  ])

  const moonset = firstValue(moon, [
    "moonset",
    "moonset_local",
  ])

  return (
    <section className="rounded-3xl border border-white/10 bg-white/[0.025] p-5 sm:p-6">
      <SectionHeader
        icon={<Moon className="h-5 w-5" />}
        eyebrow="Celestial Light"
        title="Sun & Moon"
        description="Darkness and lunar conditions during your session."
      />

      <div className="mt-6 grid grid-cols-2 gap-3 sm:grid-cols-3">
        <Metric
          
          label="Sunrise"
          value={formatValue(sunrise)}
        />
        
        <Metric
          
          label="Sunset"
          value={formatValue(sunset)}
        />

        

        <Metric
        
          label="Astronomical Dusk"
          value={formatValue(astroDusk)}
        />

        <Metric
         
          label="Astronomical Dawn"
          value={formatValue(astroDawn)}
        />

        <Metric
        
          label="Moon Phase"
          value={formatValue(phase)}
        />

        <Metric
         
          label="Moon Illumination"
          value={
            illumination !== null &&
            illumination !== undefined &&
            illumination !== ""
              ? `${Number(illumination).toFixed(1)}%`
              : "—"
          }
        />

        <Metric
        
          label="Moonrise"
          value={formatValue(moonrise)}
        />

        <Metric
          
          label="Moonset"
          value={formatValue(moonset)}
        />
      </div>
    </section>
  )
}
/* =========================================================
   OBJECT SECTION
========================================================= */

function ObjectSection({
  title,
  icon,
  description,
  objects,
  empty,
  accent,
  fallbackType,
  meteor = false,
}: {
  title: string
  icon: React.ReactNode
  description: string
  objects: any[]
  empty: string
  accent: string
  fallbackType: string
  meteor?: boolean
}) {
  return (
    <section className="rounded-3xl border border-white/10 bg-white/[0.025] p-5 sm:p-6">
      <SectionHeader
        icon={icon}
        eyebrow={`${objects.length} target${objects.length === 1 ? "" : "s"}`}
        title={title}
        description={description}
      />

      {objects.length === 0 ? (
        <div className="mt-6 rounded-2xl border border-dashed border-white/10 bg-black/10 px-4 py-8 text-center">
          <div className="text-sm text-white/35">
            {empty}
          </div>
        </div>
      ) : (
        <div className="mt-5 grid gap-3">
          {objects.map((object, index) => (
            <AstronomyObjectCard
              key={`${getObjectName(object)}-${index}`}
              object={object}
              fallbackType={fallbackType}
              accent={accent}
              meteor={meteor}
            />
          ))}
        </div>
      )}
    </section>
  )
}





function AstronomyObjectCard({
  object,
  fallbackType,
  accent,
  meteor,
}: {
  object: any
  fallbackType: string
  accent: string
  meteor?: boolean
}) {
  const name = getObjectName(object)

  const type = getObjectType(
    object,
    fallbackType
  )

  const rise = getRise(object)
  const set = getSet(object)
  const best = getBestTime(object)
  console.log("ASTRONOMY OBJECT:", object)
  console.log("BEST DATA:", object?.best)

  const peakTime = getPeakTime(object)
  const peakRate = getPeakRate(object)

  const constellation = getConstellation(object)

  const azimuth = getAzimuth(object)
  const altitude = getAltitude(object)

  const distance = normalizeDistance(
    getDistance(object)
  )

  const recommendation =
    getRecommendation(object)

  // ==========================================================
  // METEOR SHOWER DATA
  // ==========================================================

  const shower =
    object?.shower &&
    typeof object.shower === "object"
      ? object.shower
      : object

  const active =
    shower?.active &&
    typeof shower.active === "object"
      ? shower.active
      : object?.active &&
          typeof object.active === "object"
        ? object.active
        : null

  const activeStart =
    active?.start ||
    object?.active_start ||
    object?.start_date ||
    null

  const activeEnd =
    active?.end ||
    object?.active_end ||
    object?.end_date ||
    null

  const radiant =
    shower?.radiant &&
    typeof shower.radiant === "object"
      ? shower.radiant
      : object?.radiant &&
          typeof object.radiant === "object"
        ? object.radiant
        : null

  const radiantName =
    radiant?.name ||
    radiant?.constellation ||
    radiant?.constellationName ||
    constellation ||
    null

  const radiantAltitude =
    object?.radiant_altitude_deg ??
    radiant?.altitudeDeg ??
    radiant?.altitude_deg ??
    radiant?.altitude ??
    null

  const meteorVisible =
    object?.visible !== false

  const observability =
    object?.observability ||
    null

  const difficulty =
    object?.difficulty ||
    null

  const nakedEye =
    object?.naked_eye

  // ==========================================================
  // PEAK DATA
  // ==========================================================

  const peakDate =
    object?.peak_date ||
    object?.peakDate ||
    shower?.peak_date ||
    shower?.peakDate ||
    object?.peak?.date ||
    shower?.peak?.date ||
    null

  const meteorPeakTime =
    peakTime ||
    object?.peak?.time ||
    shower?.peak?.time ||
    null

  const meteorPeakRate =
    peakRate ??
    object?.peak?.rate ??
    object?.peak?.zhr ??
    shower?.peak?.rate ??
    shower?.peak?.zhr ??
    null

  // ==========================================================
  // FORMAT DATE
  // ==========================================================

  const formatMeteorDate = (value: any) => {
    if (!value) return null

    try {
      const text = String(value)

      // YYYY-MM-DD
      if (/^\d{4}-\d{2}-\d{2}$/.test(text)) {
        const date = new Date(
          `${text}T00:00:00`
        )

        return date.toLocaleDateString(
          undefined,
          {
            month: "short",
            day: "numeric",
            year: "numeric",
          }
        )
      }

      return text
    } catch {
      return String(value)
    }
  }

  const formattedActiveStart =
    formatMeteorDate(activeStart)

  const formattedActiveEnd =
    formatMeteorDate(activeEnd)

  const formattedPeakDate =
    formatMeteorDate(peakDate)

  // ==========================================================
  // FORMAT ALTITUDE
  // ==========================================================

  const formattedRadiantAltitude =
    radiantAltitude !== null &&
    radiantAltitude !== undefined &&
    !Number.isNaN(Number(radiantAltitude))
      ? `${Number(radiantAltitude).toFixed(1)}°`
      : null

  // ==========================================================
  // FORMAT NAKED EYE
  // ==========================================================

  const nakedEyeText =
    nakedEye === true
      ? "Yes"
      : nakedEye === false
        ? "No"
        : null

  return (
    <div className="group relative overflow-hidden rounded-2xl border border-white/10 bg-black/20 p-4 transition hover:border-white/15 hover:bg-white/[0.035]">

      {/* Accent */}
      <div
        className={`absolute left-0 top-0 h-full w-[2px] ${
          accent === "violet"
            ? "bg-violet-400/70"
            : accent === "blue"
              ? "bg-blue-400/70"
              : accent === "amber"
                ? "bg-amber-300/70"
                : "bg-cyan-300/70"
        }`}
      />

      {/* =====================================================
          IDENTITY
      ===================================================== */}

      <div className="flex items-start gap-3">

        <div className="mt-0.5 flex h-9 w-9 shrink-0 items-center justify-center rounded-xl border border-white/10 bg-white/[0.04]">

          {meteor ? (
            <Zap className="h-4 w-4 text-amber-300" />
          ) : (
            <Star className="h-4 w-4 text-cyan-300" />
          )}

        </div>

        <div className="min-w-0 flex-1">

          {/* Name */}
          <div className="flex flex-col gap-2 sm:flex-row sm:items-center sm:justify-between">

            <div className="min-w-0">

              <h3 className="text-sm font-semibold text-white/95">
                {name}
              </h3>

              <div className="mt-3 flex gap-2 text-xs leading-5 text-white/90">
                {type}
                {constellation
                  ? ` · ${constellation}`
                  : ""}
              </div>

            </div>

          </div>

          {/* =================================================
              AVAILABILITY
          ================================================= */}

          <div className="mt-4">

            {(() => {

              const isVisible =
                meteor
                  ? meteorVisible
                  : getAvailability(object)

              return (
                <div
                  className={`flex items-center gap-3 rounded-xl border px-4 py-3 ${
                    isVisible
                      ? "border-emerald-400/20 bg-emerald-400/[0.07]"
                      : "border-white/10 bg-white/[0.035]"
                  }`}
                >

                  <span
                    className={`h-2.5 w-2.5 shrink-0 rounded-full ${
                      isVisible
                        ? "bg-emerald-300 shadow-[0_0_12px_rgba(110,231,183,.8)]"
                        : "bg-white/35"
                    }`}
                  />

                  <div>

                    <div
                      className={`text-sm font-semibold ${
                        isVisible
                          ? "text-emerald-200"
                          : "text-white/75"
                      }`}
                    >
                      Available —{" "}
                      {isVisible
                        ? "Visible"
                        : "Not visible"}
                    </div>

                    <div className="mt-0.5 text-[10px] uppercase tracking-[0.15em] text-white/30">

                      {meteor
                        ? observability
                          ? observability.replace(
                              /_/g,
                              " "
                            )
                          : isVisible
                            ? "Meteor shower is active"
                            : "Meteor shower is not visible"
                        : isVisible
                          ? "Object is above the horizon"
                          : "Object is available but below the horizon"}

                    </div>

                  </div>

                </div>
              )

            })()}

          </div>

          {/* =================================================
              METEOR SHOWER DETAILS
          ================================================= */}

          {meteor && (
            <div className="mt-4 rounded-xl border border-amber-300/10 bg-amber-300/[0.025] p-3">

              <div className="mb-3 flex items-center gap-2">

                <Zap className="h-3.5 w-3.5 text-amber-300" />

                <span className="text-[10px] font-semibold uppercase tracking-[0.16em] text-amber-200/70">
                  Meteor Shower Details
                </span>

              </div>

              <div className="grid grid-cols-2 gap-x-4 gap-y-3 sm:grid-cols-3">

                {/* Active Period */}
                {(formattedActiveStart ||
                  formattedActiveEnd) && (
                  <div>

                    <div className="text-[10px] uppercase tracking-wider text-white/30">
                      Active Period
                    </div>

                    <div className="mt-1 text-xs font-medium text-white/75">

                      {formattedActiveStart &&
                      formattedActiveEnd
                        ? `${formattedActiveStart} – ${formattedActiveEnd}`
                        : formattedActiveStart ||
                          formattedActiveEnd}

                    </div>

                  </div>
                )}

                {/* Peak Date */}
                {formattedPeakDate && (
                  <div>

                    <div className="text-[10px] uppercase tracking-wider text-white/30">
                      Peak Date
                    </div>

                    <div className="mt-1 text-xs font-medium text-white/75">
                      {formattedPeakDate}
                    </div>

                  </div>
                )}

                {/* Peak Time */}
                {meteorPeakTime && (
                  <div>

                    <div className="text-[10px] uppercase tracking-wider text-white/30">
                      Peak Time
                    </div>

                    <div className="mt-1 text-xs font-medium text-white/75">
                      {formatObservationTime(
                        meteorPeakTime
                      )}
                    </div>

                  </div>
                )}

                {/* Peak Rate */}
                {meteorPeakRate !== null &&
                  meteorPeakRate !== undefined && (
                    <div>

                      <div className="text-[10px] uppercase tracking-wider text-white/30">
                        Peak Rate
                      </div>

                      <div className="mt-1 text-xs font-medium text-white/75">
                        {meteorPeakRate} meteors/hr
                      </div>

                    </div>
                  )}

                {/* Radiant */}
                {radiantName && (
                  <div>

                    <div className="text-[10px] uppercase tracking-wider text-white/30">
                      Radiant
                    </div>

                    <div className="mt-1 text-xs font-medium text-white/75">
                      {radiantName}
                    </div>

                  </div>
                )}

                {/* Radiant Altitude */}
                {formattedRadiantAltitude && (
                  <div>

                    <div className="text-[10px] uppercase tracking-wider text-white/30">
                      Radiant Altitude
                    </div>

                    <div className="mt-1 text-xs font-medium text-white/75">
                      {formattedRadiantAltitude}
                    </div>

                  </div>
                )}

                {/* Naked Eye */}
                {nakedEyeText && (
                  <div>

                    <div className="text-[10px] uppercase tracking-wider text-white/30">
                      Naked Eye
                    </div>

                    <div className="mt-1 text-xs font-medium text-white/75">
                      {nakedEyeText}
                    </div>

                  </div>
                )}

                {/* Difficulty */}
                {difficulty && (
                  <div>

                    <div className="text-[10px] uppercase tracking-wider text-white/30">
                      Difficulty
                    </div>

                    <div className="mt-1 text-xs font-medium capitalize text-white/75">
                      {String(
                        difficulty
                      ).replace(
                        /_/g,
                        " "
                      )}
                    </div>

                  </div>
                )}

              </div>

            </div>
          )}

          {/* =================================================
              NORMAL ASTRONOMY INFORMATION
          ================================================= */}

          {!meteor && (
            <div className="mt-4 border-t border-white/5 pt-3">

              <div className="flex flex-wrap gap-x-4 gap-y-1.5 text-sm text-white/60">

                {rise && (
                  <span>
                    <strong className="text-white/65">
                      Rise
                    </strong>{" "}
                    {formatObservationTime(rise)}
                  </span>
                )}

                {set && (
                  <span>
                    <strong className="text-white/65">
                      Set
                    </strong>{" "}
                    {formatObservationTime(set)}
                  </span>
                )}

                {best && (
                  <span>
                    <strong className="text-white/65">
                      Best
                    </strong>{" "}
                       {formatObservationTime(best)}
                  </span>
                )}

                {azimuth && (
                  <span>
                    <strong className="text-white/65">
                      Az
                    </strong>{" "}
                    {azimuth}
                  </span>
                )}

                {altitude && (
                  <span>
                    <strong className="text-white/65">
                      Alt
                    </strong>{" "}
                    {altitude}
                  </span>
                )}

                {distance && (
                  <span>
                    <strong className="text-white/65">
                      Distance
                    </strong>{" "}
                    {distance}
                  </span>
                )}

              </div>

            </div>
          )}

          {/* =================================================
              METEOR OBSERVATION INFO
          ================================================= */}

          {meteor && (
            <div className="mt-3 flex flex-wrap gap-x-4 gap-y-1.5 border-t border-white/5 pt-3 text-sm text-white/60">

              {best && (
                <span>
                  <strong className="text-white/65">
                    Best observation
                  </strong>{" "}
                  {formatObservationTime(best)}
                </span>
              )}

              {azimuth && (
                <span>
                  <strong className="text-white/65">
                    Az
                  </strong>{" "}
                  {azimuth}
                </span>
              )}

              {altitude && (
                <span>
                  <strong className="text-white/65">
                    Alt
                  </strong>{" "}
                  {altitude}
                </span>
              )}

            </div>
          )}

          {/* =================================================
              RECOMMENDATION
          ================================================= */}

          {recommendation && (
            <div className="mt-3 flex gap-2 text-xs leading-5 text-white">

              <Sparkles className="mt-0.5 h-3.5 w-3.5 shrink-0 text-cyan-300/60" />

              <span>
                {recommendation}
              </span>

            </div>
          )}

        </div>

      </div>

    </div>
  )
}
/* =========================================================
   EVENTS
========================================================= */

function AstronomicalEvents({
  data,
}: {
  data: any
}) {
  const events =
    data?.astronomical_events ||
    data?.astronomicalEvents ||
    data?.events ||
    {}

  const groups = [
    {
      title: "Eclipses",
      items: getArray(events, ["eclipses"]),
    },
    {
      title: "Conjunctions",
      items: getArray(events, ["conjunctions"]),
    },
    {
      title: "Oppositions",
      items: getArray(events, ["oppositions"]),
    },
    {
      title: "Occultations",
      items: getArray(events, ["occultations"]),
    },
  ]

  const total = groups.reduce(
    (sum, group) => sum + group.items.length,
    0
  )

  return (
    <section className="rounded-3xl border border-white/10 bg-white/[0.025] p-5 sm:p-6">
      <SectionHeader
        icon={<Zap className="h-5 w-5" />}
        eyebrow={`${total} event${total === 1 ? "" : "s"}`}
        title="Astronomical Events"
        description="Major celestial events occurring during your selected session."
      />

      {total === 0 ? (
        <div className="mt-5 flex items-center gap-3 rounded-2xl border border-white/5 bg-black/15 p-4">
          <CheckCircle2 className="h-5 w-5 text-cyan-300/70" />

          <div>
            <div className="text-sm font-medium">
              No major events
            </div>

            <div className="mt-3 flex gap-2 text-xs leading-5 text-white/40">
              No eclipses, conjunctions, oppositions or
              occultations were detected in this observation
              window.
            </div>
          </div>
        </div>
      ) : (
        <div className="mt-5 grid gap-3 sm:grid-cols-2">
          {groups.flatMap((group) =>
            group.items.map(
              (event: any, index: number) => (
                <div
                  key={`${group.title}-${index}`}
                  className="rounded-2xl border border-white/10 bg-black/20 p-4"
                >
                  <div className="text-[10px] uppercase tracking-[0.18em] text-cyan-300/50">
                    {group.title}
                  </div>

                  <div className="mt-2 font-medium">
                    {getObjectName(event)}
                  </div>

                  <div className="mt-2 text-sm leading-6 text-white/90">
                    {formatValue(
                      firstValue(event, [
                        "date",
                        "time",
                        "datetime",
                      ])
                    )}
                  </div>
                </div>
              )
            )
          )}
        </div>
      )}
    </section>
  )
}

/* =========================================================
   AI RECOMMENDATION
========================================================= */

function AIRecommendation({
  data,
}: {
  data: any
}) {
  const recommendation =
    data?.ai_recommendation ||
    data?.recommendation ||
    data?.ai ||
    {}

  const score = recommendation?.score

  return (
    <section className="relative overflow-hidden rounded-3xl border border-violet-400/10 bg-violet-400/[0.035] p-5 sm:p-7">
      <div className="absolute right-[-100px] top-[-100px] h-[300px] w-[300px] rounded-full bg-violet-500/10 blur-[100px]" />

      <div className="relative">
        <div className="flex flex-col gap-5 sm:flex-row sm:items-start sm:justify-between">
          <div>
            <div className="flex items-center gap-2 text-xs uppercase tracking-[0.22em] text-violet-300/60">
              <Sparkles className="h-4 w-4" />
              Astronomy Intelligence
            </div>

            <h2 className="mt-2 text-xl font-semibold">
              AI Observation Recommendation
            </h2>
          </div>

          {score !== null &&
            score !== undefined && (
              <div className="flex h-16 w-16 shrink-0 flex-col items-center justify-center rounded-2xl border border-violet-300/15 bg-violet-300/[0.06]">
                <span className="text-lg font-semibold text-violet-200">
                  {score}
                </span>
                <span className="text-[9px] uppercase tracking-wider text-white/90">
                  / 10
                </span>
              </div>
            )}
        </div>

        {recommendation?.recommendation && (
          <p className="relative mt-5 max-w-4xl text-sm leading-7 text-white/90">
            {recommendation.recommendation}
          </p>
        )}

        {Array.isArray(recommendation?.best_targets) &&
          recommendation.best_targets.length > 0 && (
            <div className="relative mt-5">
              <div className="mb-2 text-[15px] uppercase tracking-[0.2em] text-white/90">
                Recommended Targets
              </div>
              <div className="flex flex-wrap gap-2">
                {recommendation.best_targets.map((target: any, index: number) => (
                  <div
                    key={`${getObjectName(target)}-${index}`}
                    className="rounded-full border border-violet-300/10 bg-violet-300/[0.05] px-3 py-1.5 text-xs text-violet-100/70"
                  >
                    {getObjectName(target)}
                  </div>
                ))}
              </div>
            </div>
          )}

        <div className="relative mt-5 grid gap-3 md:grid-cols-3">
          {recommendation?.best_time && (
            <AIInfo
              label="Best Time"
              value={recommendation.best_time}
            />
          )}

          {recommendation?.weather_summary && (
            <AIInfo
              label="Weather"
              value={recommendation.weather_summary}
            />
          )}

          {recommendation?.astronomy_summary && (
            <AIInfo
              label="Astronomy"
              value={recommendation.astronomy_summary}
            />
          )}
        </div>

        {Array.isArray(recommendation?.tips) &&
          recommendation.tips.length > 0 && (
            <div className="relative mt-5 flex flex-wrap gap-2">
              {recommendation.tips.map(
                (tip: string, index: number) => (
                  <div
                    key={index}
                    className="rounded-full border border-white/10 bg-black/20 px-3 py-1.5 text-xs text-white/90"
                  >
                    {tip}
                  </div>
                )
              )}
            </div>
          )}
      </div>
    </section>
  )
}

/* =========================================================
   LOCATION EDITOR
========================================================= */

function LocationEditor({
  location,
  setLocation,
  onClose,
  onSave,
  onUseCurrent,
}: {
  location: LocationData
  setLocation: React.Dispatch<
    React.SetStateAction<LocationData>
  >
  onClose: () => void
  onSave: () => void
  onUseCurrent: () => void
}) {
  return (
    <div className="fixed inset-0 z-[100] flex items-center justify-center bg-black/75 p-4 backdrop-blur-sm">
      <div className="w-full max-w-lg rounded-3xl border border-white/10 bg-[#090c14] p-5 shadow-2xl sm:p-6">
        <div className="flex items-start justify-between">
          <div>
            <div className="flex items-center gap-2 text-xs uppercase tracking-[0.2em] text-cyan-300/60">
              <MapPin className="h-4 w-4" />
              Location
            </div>

            <h2 className="mt-2 text-xl font-semibold">
              Choose observation location
            </h2>
          </div>

          <button
            onClick={onClose}
            className="rounded-xl p-2 text-white/40 hover:bg-white/5 hover:text-white"
          >
            <X className="h-5 w-5" />
          </button>
        </div>

        <button
          onClick={onUseCurrent}
          className="mt-6 flex w-full items-center gap-3 rounded-2xl border border-cyan-400/15 bg-cyan-400/[0.05] p-4 text-left hover:bg-cyan-400/[0.08]"
        >
          <Navigation className="h-5 w-5 text-cyan-300" />

          <div>
            <div className="text-sm font-medium">
              Use my current location
            </div>

            <div className="mt-1 text-xs text-white/35">
              Use your device GPS coordinates.
            </div>
          </div>
        </button>

        <div className="my-5 flex items-center gap-3">
          <div className="h-px flex-1 bg-white/10" />
          <span className="text-[10px] uppercase tracking-wider text-white/25">
            or enter coordinates
          </span>
          <div className="h-px flex-1 bg-white/10" />
        </div>

        <div className="space-y-4">
          <InputField
            label="Location name"
            value={location.name}
            onChange={(value) =>
              setLocation((prev) => ({
                ...prev,
                name: value,
              }))
            }
          />

          <div className="grid grid-cols-2 gap-3">
            <InputField
              label="Latitude"
              type="number"
              step="any"
              value={location.latitude}
              onChange={(value) =>
                setLocation((prev) => ({
                  ...prev,
                  latitude: Number(value),
                }))
              }
            />

            <InputField
              label="Longitude"
              type="number"
              step="any"
              value={location.longitude}
              onChange={(value) =>
                setLocation((prev) => ({
                  ...prev,
                  longitude: Number(value),
                }))
              }
            />
          </div>
        </div>

        <div className="mt-6 flex gap-3">
          <Button
            variant="outline"
            onClick={onClose}
            className="flex-1 border-white/10 bg-white/[0.03]"
          >
            Cancel
          </Button>

          <Button
            onClick={onSave}
            className="flex-1 bg-cyan-400 text-black hover:bg-cyan-300"
          >
            Save location
          </Button>
        </div>
      </div>
    </div>
  )
}

/* =========================================================
   SMALL COMPONENTS
========================================================= */

function SectionHeader({
  icon,
  eyebrow,
  title,
  description,
}: {
  icon: React.ReactNode
  eyebrow: string
  title: string
  description: string
}) {
  return (
    <div>
      <div className="flex items-center gap-2 text-[10px] uppercase tracking-[0.2em] text-cyan-300/50">
        {icon}
        {eyebrow}
      </div>

      <h2 className="mt-2 text-lg font-semibold tracking-tight">
        {title}
      </h2>

      <p className="mt-1 text-xs leading-5 text-white/30">
        {description}
      </p>
    </div>
  )
}

function DateTimeField({
  label,
  icon,
  type,
  value,
  min,
  onChange,
}: any) {
  return (
    <label className="block">
      <div className="mb-2 flex items-center gap-2 text-xs text-white/40">
        {icon}
        {label}
      </div>

      <input
        type={type}
        value={value}
        min={min}
        onChange={(e) => onChange(e.target.value)}
        className="h-11 w-full rounded-xl border border-white/10 bg-black/20 px-3 text-sm text-white outline-none transition focus:border-cyan-400/40 focus:ring-2 focus:ring-cyan-400/10"
      />
    </label>
  )
}

function TimeSelectField({
  label,
  icon,
  value,
  onChange,
}: {
  label: string
  icon: React.ReactNode
  value: string
  onChange: (value: string) => void
}) {
  const timeOptions = generateTimeOptions()

  return (
    <label className="block">
      <div className="mb-2 flex items-center gap-2 text-xs text-white/40">
        {icon}
        {label}
      </div>

      <select
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="h-11 w-full rounded-xl border border-white/10 bg-black/20 px-3 text-sm text-white outline-none transition focus:border-cyan-400/40 focus:ring-2 focus:ring-cyan-400/10"
      >
        {timeOptions.map((time) => (
          <option
            key={time.value}
            value={time.value}
            className="bg-[#090c14] text-white"
          >
            {time.label}
          </option>
        ))}
      </select>
    </label>
  )
}

function InputField({
  label,
  value,
  onChange,
  type = "text",
  step,
}: {
  label: string
  value: string | number
  onChange: (value: string) => void
  type?: string
  step?: string
}) {
  return (
    <label className="block">
      <div className="mb-2 text-xs text-white/40">
        {label}
      </div>

      <input
        type={type}
        step={step}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="h-11 w-full rounded-xl border border-white/10 bg-black/20 px-3 text-sm text-white outline-none focus:border-cyan-400/40"
      />
    </label>
  )
}

function SummaryBox({
  icon,
  label,
  value,
  accent,
  labelClassName,
  valueClassName,

}: {
  icon: React.ReactNode
  label: string
  value: string
  accent: string
  labelClassName?: string
  valueClassName?: string
}) {
  return (
    <div className="rounded-2xl border border-white/10 bg-black/20 p-4">
      <div className="flex items-center gap-2 text-xs text-white/35">
        <span
          className={
            accent === "violet"
              ? "text-violet-300"
              : accent === "blue"
                ? "text-blue-300"
                : accent === "amber"
                  ? "text-amber-300"
                  : "text-cyan-300"
          }
        >
          {icon}
        </span>

        {label}
      </div>

      <div className="mt-3 text-2xl font-semibold tracking-tight">
        {value}
      </div>
    </div>
  )
}


function Metric({
  label,
  value,
  large = false,
}: {
  label: string
  value: string
  large?: boolean
}) {
  return (
    <div className="rounded-2xl border border-white/5 bg-black/15 p-3">
      <div
        className={
          large
            ? "text-xs uppercase tracking-wider text-white"
            : "text-[12px] uppercase tracking-wider text-white/90"
        }
      >
        {label}
      </div>

      <div
        className={
          large
            ? "mt-1.5 truncate text-lg font-semibold text-white"
            : "mt-1.5 truncate text-sm font-medium text-white/80"
        }
      >
        {value}
      </div>
    </div>
  )
}

function StatusPill({
  children,
  positive = false,
}: {
  children: React.ReactNode
  positive?: boolean
}) {
  return (
    <span
      className={`
        inline-flex items-center gap-1.5 rounded-full border
        px-2.5 py-1 text-[10px]
        ${
          positive
            ? "border-emerald-400/15 bg-emerald-400/[0.06] text-emerald-300"
            : "border-white/10 bg-white/[0.025] text-white/45"
        }
      `}
    >
      {positive && (
        <span className="h-1.5 w-1.5 rounded-full bg-emerald-300" />
      )}

      {children}
    </span>
  )
}

function AIInfo({
  label,
  value,
}: {
  label: string
  value: string
}) {
  return (
    <div className="rounded-2xl border border-white/5 bg-black/15 p-3">
      <div className="text-xs uppercase tracking-wider text-white/30">
        {label}
      </div>

      <div className="mt-1 text-sm font-medium text-white/80">
        {value}
      </div>
    </div>
  )
}

function OverviewRow({
  label,
  value,
}: {
  label: string
  value: any
}) {
  return (
    <div className="flex items-center justify-between rounded-xl border border-white/5 bg-black/15 px-4 py-3">
      <span className="text-xs text-white/40">
        {label}
      </span>

      <span className="text-sm font-medium text-white/75">
        {value}
      </span>
    </div>
  )
}

function EmptyView({
  title,
  description,
  icon,
}: {
  title: string
  description: string
  icon: React.ReactNode
}) {
  return (
    <div className="flex min-h-[70vh] items-center justify-center">
      <div className="max-w-lg text-center">
        <div className="mx-auto flex h-16 w-16 items-center justify-center rounded-3xl border border-cyan-400/10 bg-cyan-400/5 text-cyan-300">
          {icon}
        </div>

        <h1 className="mt-5 text-2xl font-semibold">
          {title}
        </h1>

        <p className="mt-2 text-sm leading-6 text-white/35">
          {description}
        </p>
      </div>
    </div>
  )
}

/* =========================================================
   API RESPONSE ADAPTERS
========================================================= */

function getPlanets(data: any) {
  return getArray(data?.planets, [
    "objects",
    "planets",
  ])
    .concat(
      Array.isArray(data?.modules?.planets)
        ? data.modules.planets
        : []
    )
}

function getDeepSky(data: any) {
  return getArray(data?.deep_sky, [
    "objects",
    "targets",
  ])
    .concat(
      getArray(data?.deepSky, [
        "objects",
        "targets",
      ])
    )
}

function getConstellations(data: any) {
  return getArray(data?.constellations, [
    "objects",
    "targets",
    "visible",
    "results",
    "data",
    "constellations",
  ]).concat(
    getArray(data?.constellation, ["objects", "targets", "results", "data"])
  )
}



function getMeteorShowers(data: any) {
  console.log("FULL OBSERVATION DATA:", data)

  console.log("meteor_showers:", data?.meteor_showers)

  console.log("meteorShowers:", data?.meteorShowers)

  const showers1 = getArray(data?.meteor_showers, [
    "showers",
    "objects",
    "active",
    "results",
    "data",
    "meteor_showers",
  ])

  const showers2 = getArray(data?.meteorShowers, [
    "showers",
    "objects",
    "active",
    "results",
    "data",
  ])

  console.log("SHOWERS FROM meteor_showers:", showers1)
  console.log("SHOWERS FROM meteorShowers:", showers2)

  return [...showers1, ...showers2]
}
