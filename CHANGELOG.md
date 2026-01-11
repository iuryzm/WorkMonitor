# Changelog

All notable changes to this project will be documented in this file.


## [Unreleased]

### Added
- Criar uma entrada a mais no menu do botão direito do mouse no system tray.
    - Esse menu deve se chagar Relatório.
    - Ao clicar em Relatório deve-se abrir um html.
        - O html deve oferecer a opção de criar o relatório num certo período.
            - Dados do mês passado.
            - Dados do ano passado.
            - Período entre duas datas.
        - 1a parte do relatório contabilizará o número de registros de cada tipo dentro do período.
        - 2a parte do relatório mostrará um gráfico relacionado a 1a parte.
        - 3a parte criar uma tabela mostrando quantas horas foram trabalhadas em cada atividade em cada dia no período.
            - Iremos considerar que cada dia possui 8 horas e o tempo em cada atividade no dia será dado por 8 horas divido pelo número de registros de atividade no dia.
        - O relatório deve ser salvo em um arquivo html contendo em seu nome o período usado na entrada e a data e hora na qual ele foi criado.

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
