import { RouteObject } from "react-router-dom";

import { App } from "../pages/top/components/app";

export const routes: RouteObject[] = [
  {
    path: "/",
    element: <App />,
  },
];
