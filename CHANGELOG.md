# Changelog

All notable changes to this project will be documented in this file.


## [Unreleased]

### Added
- Mostrar quanto tempo falta para aparecer na tela a próxima janela de registro de atividade, ou que horas ela irá aparecer.
- build_windows.bat poderia criar um atalho para o executável criado em shell:startup, ou ao menos perguntar ao usuário se ele deseja isso.

## [0.2.0] - 2026-01-13

### Added
- Adicionada opção "Relatório" no menu do ícone da bandeja (system tray).
- Implementada funcionalidade de geração de relatórios em HTML.
    - Gera um arquivo visual com dados de atividades.
    - Permite visualização de registros e estatísticas.

### Changed
- 

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
