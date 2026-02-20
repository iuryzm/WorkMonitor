# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- Criar uma entrada no menu que aparece ao apertar o botão direito no ícone da bandeja (system tray) para editar o arquivo work_log.csv. Deve-se abrir o arquivo no editor de texto padrão do sistema.

## [0.3.1] - 2026-02-05

### Changed
- **Timer Logic**: The interval timer is now reset automatically when a "New Entry" is manually requested, and restarted when an activity is submitted.
- **Data Persistence**: Activity logs are now stored in the user's home directory (`~/.workmonitor/work_log.csv`) instead of the application directory. This ensures data is preserved across application updates/builds.
- **UI Improvements**: 
    - The activity input window now uses a standard window frame (title bar, minimize/close buttons) for better OS integration.
    - Updated styles for a cleaner look.
    - Added clear "History" label to the history button.

## [0.3.0] - 2026-02-05

### Added
- Countdown timer in system tray tooltip showing time until next prompt.
- Option to create a desktop shortcut in the Windows Startup folder during build (`build_windows.bat`).
- Activity History navigation:
    - Up/Down arrow keys to cycle through recent activities in the input window.
    - Dropdown button to select from unique past activities.

## [0.2.0] - 2026-01-13

### Added
- Adicionada opção "Relatório" no menu do ícone da bandeja (system tray).
- Implementada funcionalidade de geração de relatórios em HTML.
    - Gera um arquivo visual com dados de atividades.
    - Permite visualização de registros e estatísticas.

## [0.1.1] - 2026-01-10

### Added
- Criar um README.md

## [0.1.0] - 2026-01-09

### Added
- Initial release of WorkMonitor.
- Core functionality:
    - Periodic activity prompts (overlay window).
    - Activity logging to `work_log.csv`.
    - Autocomplete based on history.
- System Tray integration:
    - New Entry, Pause/Resume, Settings, Exit.
- Settings management:
    - Configurable interval.
    - Sound toggle.
- Cross-platform support (Linux/Windows) using PySide6.
