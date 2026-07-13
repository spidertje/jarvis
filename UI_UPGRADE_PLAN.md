# JARVIS UI Upgrade Plan

Goal: Make jarvis.html stand out with Mark-XXXIX-OR inspired visual elements.

## Current State
- Single-column chat layout
- Basic settings panel
- Simple status indicators
- Static background with scanlines
- Minimal animations

## Proposed Upgrades

### 1. Enhanced HUD Background
- **Inspiration**: Mark's `HudCanvas` widget
- **Implementation**: 
  - Add canvas-based animated background with rotating arcs
  - Pulsing energy rings that react to voice/TTS activity
  - Subtle particle effects
  - Status-reactive color changes (cyan=active, green=listening, yellow=thinking)

### 2. Three-Panel Layout
- **Inspiration**: Mark's MainWindow with left/right panels
- **Implementation**:
  - Left panel: Quick actions, recent files, system status
  - Center: Chat area (current)
  - Right panel: Context, memory, file info
  - Responsive: collapse to single column on mobile

### 3. System Metrics Dashboard
- **Inspiration**: Mark's `_SysMetrics` and `MetricBar` widgets
- **Implementation**:
  - Real-time CPU, RAM, network usage bars
  - Temperature monitoring (if API available)
  - Animated progress bars with color coding
  - Auto-updating every 2-3 seconds

### 4. Enhanced File Drop Zone
- **Inspiration**: Mark's `FileDropZone` widget
- **Implementation**:
  - Drag-and-drop with visual feedback
  - File type icons (image, PDF, code, audio, video)
  - Preview thumbnails for images
  - Processing status indicators
  - File history list

### 5. Animated Status Indicators
- **Inspiration**: Mark's color-coded status system
- **Implementation**:
  - Large center status indicator (listening/thinking/speaking)
  - Pulsing animations that react to voice activity
  - Color transitions between states
  - Waveform visualizer during voice input

### 6. Tool/Action Buttons
- **Inspiration**: Mark's action buttons
- **Implementation**:
  - Quick access buttons for common tasks
  - Web search, weather, file operations
  - Expandable action menu
  - Keyboard shortcuts display

### 7. Session/Conversation Management
- **Inspiration**: Mark's conversation handling
- **Implementation**:
  - Save/load conversation sessions
  - Export chat history (JSON, Markdown, PDF)
  - Session search/filter
  - Recent conversations list

### 8. Transparency/Theme Controls
- **Inspiration**: Mark's `SetupOverlay`
- **Implementation**:
  - Slider for UI transparency
  - Multiple color themes (cyan, green, purple, orange)
  - Accent color picker
  - Font size controls

## Implementation Order

1. **Phase 1**: Enhanced HUD background + animated status indicators
2. **Phase 2**: System metrics dashboard (if API available)
3. **Phase 3**: Enhanced file drop zone
4. **Phase 4**: Three-panel layout
5. **Phase 5**: Tool/action buttons
6. **Phase 6**: Session management
7. **Phase 7**: Theme controls

## Technical Notes
- Use Canvas API for background animations
- CSS animations for status indicators
- Fetch API for system metrics (if endpoint available)
- LocalStorage for session persistence
- File API for drag-and-drop
- Responsive CSS Grid/Flexbox for layout
