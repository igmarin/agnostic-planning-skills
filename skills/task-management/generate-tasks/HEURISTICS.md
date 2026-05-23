# First-Slice Heuristics

Use the smallest slice that proves behavior at the right boundary:

| Change type | Default first slice |
|-------------|---------------------|
| New endpoint or API behavior | Request/integration test -> handler/service wiring -> persistence/docs |
| New service or domain rule | Service or unit test -> implementation -> callers/docs |
| Background work | Job/worker test -> service/domain test if logic is substantial |
| External integration | Client/fetcher layer test -> builder/domain mapping -> callers |
| UI component or page | Component/render test -> component implementation -> integration |
| Library / SDK | Public API test -> implementation -> docs/examples |
| Bug fix | Highest-value reproducing test at the boundary where users feel the bug |

When in doubt, prefer the highest-value failing test that proves the user-visible behavior before descending into lower-level units.
