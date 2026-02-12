from pydantic import BaseModel, Field
from typing import List, Union, Literal

# 1. Define a "Stat Card" (e.g., "Total Revenue: $50k")
class StatCard(BaseModel):
    type: Literal["stat_card"] = "stat_card"
    title: str = Field(..., description="The label of the statistic (e.g. 'Active Users')")
    value: str = Field(..., description="The value to display (e.g. '1,200')")
    trend: str = Field(None, description="Optional trend indicator (e.g. '+5%')")

# 2. Define a "Chart" (e.g., A line graph)
class ChartData(BaseModel):
    type: Literal["chart_line"] = "chart_line"
    title: str = Field(..., description="Title of the chart")
    labels: List[str] = Field(..., description="X-axis labels (e.g. ['Jan', 'Feb', 'Mar'])")
    data: List[int] = Field(..., description="Y-axis data points (e.g. [10, 20, 15])")

# 3. Define the "Dashboard" (The container for everything)
class DashboardUI(BaseModel):
    title: str = Field(..., description="The main title of the generated dashboard")
    components: List[Union[StatCard, ChartData]] = Field(..., description="List of UI components to render")