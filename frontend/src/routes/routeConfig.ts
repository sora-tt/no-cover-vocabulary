/**
 * Route configuration
 */
export const routeConfig = {
  TOP: "/",
  NO_COVER_VOCABULARY: "/no-cover-vocabulary",
} as const;

export type RoutePath = (typeof routeConfig)[keyof typeof routeConfig];

/**
 * Feature ID to Route Path mapping
 */
export const featureRouteMap = {
  noCoverVocabulary: routeConfig.NO_COVER_VOCABULARY,
} as const;

export type FeatureId = keyof typeof featureRouteMap;

/**
 * Get Route Path by Feature ID
 * @param featureId
 * @returns RoutePath or null if not found
 */
export const getRouteByFeatureId = (featureId: FeatureId): RoutePath => {
  return featureRouteMap[featureId as FeatureId] || null;
};
