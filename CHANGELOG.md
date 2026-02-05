# Changelog

All notable changes to this project will be documented in this file.


## [Unreleased]

### Changed
- Ao colocar uma nova entrada a partir do uso da opção "New Entry" devemos reiniciar o tempo para a janela de nova atividade aparecer automaticamente.
- Quando usarmos o build o arquivo work_log.csv não pode ser apagado, devemos manter o arquivo se já existir um.
- Na janela de registro de nova atividade o botão "Show History" está sem label, vejo apenas o tooltip.
- Precisamos de um visual melhor na janela de registro de nova atividade, deixando uma janela normal de um aplicativo, com fundo, barra de título e moldura.

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
