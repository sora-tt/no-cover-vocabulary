import { createBrowserRouter } from "react-router-dom";

import { AppLayout } from "./sub-components/app-layout";
import { RootErrorBoundary } from "./sub-components/root-error-boundary";
import { App } from "../../../pages/top/components/app";
import { routeConfig } from "../../routeConfig";

export const useAppRouter = () => {
  const router = createBrowserRouter([
    {
      path: "/",
      element: <AppLayout />,
      errorElement: <RootErrorBoundary />,
      children: [
        /**
         * If you create a new page component, please add the route here.
         */
        { path: routeConfig.TOP, element: <App /> },
      ],
    },
  ]);
  return { router };
};
