import * as React from "react";
import { Outlet } from "react-router-dom";

export const AppLayout: React.FC = () => {
  return (
    <div className="app-layout">
      <Outlet />
    </div>
  );
};
