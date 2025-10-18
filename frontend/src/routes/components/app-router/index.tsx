import * as React from "react";
import { RouterProvider } from "react-router";

import { useAppRouter } from "./hooks";

export const AppRouter: React.FC = () => {
  const { router } = useAppRouter();

  return <RouterProvider router={router} />;
};
